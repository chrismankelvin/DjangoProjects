# from django import template

# @register.simple_tag
# def render_field(field):
#     template = """
#     <div>
#         <label for="{{ field.id_for_label }}">{{ field.label }}</label>
#         {{ field }}
#         {% if field.errors %}
#             <ul class="errorlist">
#                 {% for error in field.errors %}
#                     <li>{{ error }}</li>
#                 {% endfor %}
#             </ul>
#         {% endif %}
#     </div>
#     """
#     return template.format(field=field)

# @register.simple_tag
# def render_form(form):
#     template = """
#     <div>
#         <form method="post">
#             {% csrf_token %}
#             <fieldset>
#                 <legend>Join Today</legend>
#                 {% for field in form %}
#                     {% render_field field %}
#                 {% endfor %}
#             </fieldset>
#             <button type="submit">Sign Up</button>
#         </form>
#         <div>
#             <small>Already have an account?</small>
#             <a href="#">Log In</a>
#         </div>
#     </div>
#     """
#     return template.format(form=form)
