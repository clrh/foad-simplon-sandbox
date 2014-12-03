class FormsController < ApplicationController
  def index
  end
  
  def create
    @form = Form.new(form_params)
    @form.save
    redirect_to form_path
  end
   
  private
    def form_params
        params.require(:form).permit(:title, :comment)
    end
end
