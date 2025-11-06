require 'net/http'
require 'json'

class BlogsController < ApplicationController
  before_action :set_blog, only: %i[show edit update destroy]

  # GET /blogs or /blogs.json
  def index
    @blogs = Blog.all
  end

  # ✅ AI Blog Generation Endpoint
  def generate_ai
    titles = params[:titles].to_s.split("\n").map(&:strip).reject(&:empty?)
    @generated_blogs = []

    api_key = ENV['GEMINI_API_KEY'] || "YOUR_API_KEY_HERE"

    titles.each do |title|
      prompt = 
      <<~PROMPT
      " You are an expert software engineer and technical writer who creates detailed, professional blog articles for a tech website.

  ✳️ **Your task:**
  Write a complete, long-form, expert-level blog post on the topic provided below.

  ✳️ **Tone and Style:**
  - Write as if you're an experienced developer sharing insights with other developers.
  - Use a clear, confident, and engaging tone — informative, but never robotic.
  - Begin with a strong hook or relatable thought.
  - Explain complex ideas clearly, using analogies, examples, and context.
  - Flow naturally between sections — no need for headings like “## Introduction”.
  - Keep paragraphs short and readable for a blog layout.
  - When showing code, use properly formatted code blocks (triple backticks with language identifier).
  - Write in a human, editorial style — like a polished piece in a tech magazine.

  ✳️ **Structure:**
  - Opening hook paragraph
  - Background or context
  - Explanation of core concepts
  - Real-world use cases or examples
  - Optional code examples with correct syntax highlighting
  - Common challenges or considerations
  - Closing reflection or call to discussion

  ✳️ **Formatting Rules:**
  - Do **not** use Markdown symbols like `#`, `##`, `*`, or `_`.
  - Do **not** include lists with `-` or `*`; instead, use natural paragraph flow or numbered examples.
  - Code blocks should be inside triple backticks, like:
    ```python
    print("Hello, world!")
    ```
  - Avoid generic filler phrases like “In conclusion.” End with a natural, reflective statement.

  ✳️ **Topic:**
  #{title}

  ✳️ **Example style to follow:**
  “Unleashing the Serpent: Why Python Continues to Dominate the Software Landscape” — 
  narrative flow, thoughtful transitions, expert voice, and clear examples.

  Now, write the complete article."
  PROMPT

      uri = URI("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key=#{ENV['GEMINI_API_KEY']}")
      response = Net::HTTP.post(
        uri,
        { contents: [{ parts: [{ text: prompt }] }] }.to_json,
        "Content-Type" => "application/json"
      )

      content = begin
        JSON.parse(response.body).dig("candidates", 0, "content", "parts", 0, "text")
      rescue
        "No content generated."
      end

      blog = Blog.create!(title: title, content: content)
      @generated_blogs << blog
    end

    flash[:notice] = "#{@generated_blogs.count} blog(s) generated successfully!"
    redirect_to blogs_path
  end

  # GET /blogs/1
  def show; end

  # GET /blogs/new
  def new
    @blog = Blog.new
  end

  # GET /blogs/1/edit
  def edit; end

  # POST /blogs
  def create
    @blog = Blog.new(blog_params)

    respond_to do |format|
      if @blog.save
        format.html { redirect_to @blog, notice: "Blog was successfully created." }
        format.json { render :show, status: :created, location: @blog }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @blog.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /blogs/1
  def update
    respond_to do |format|
      if @blog.update(blog_params)
        format.html { redirect_to @blog, notice: "Blog was successfully updated.", status: :see_other }
        format.json { render :show, status: :ok, location: @blog }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @blog.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /blogs/1
  def destroy
    @blog.destroy!
    respond_to do |format|
      format.html { redirect_to blogs_path, notice: "Blog was successfully destroyed.", status: :see_other }
      format.json { head :no_content }
    end
  end

  private

  def set_blog
    @blog = Blog.find(params[:id])
  end

  def blog_params
    params.require(:blog).permit(:title, :content)
  end
end
