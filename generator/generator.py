from definitions import Form
from form_descriptions import FORMS
from generator_functions import (
    generate_form_columns,
    generate_form_fields,
    generate_table_headers,
    generate_form_fields_data,
    generate_main_params,
    generate_main_params_and_values,
    generate_main_values,
    generate_model_fields,
    update_component_meta_info,
    create_component_meta_info,
    manufacturers_query,
    warrantys_query,
    component_meta_info_query,
)


forms = []
for form in FORMS:
    forms.append(Form(form))
for form in forms:
    form_columns = generate_form_columns(form.fields)
    form_fields = generate_form_fields(form.fields)
    table_headers = generate_table_headers(form.fields)
    form_field_data = generate_form_fields_data(form.fields)
    main_params = generate_main_params(form.fields, form.type_)
    main_params_and_values = generate_main_params_and_values(form.fields,
                                                             form.type_)
    main_values = generate_main_values(form.fields, form.type_)
    model_fields = generate_model_fields(form.fields, form.type_)
    with open('template.vue', 'r') as file:
        template = file.read()
    template = template.replace('|model_s|', form.model.model_s)
    template = template.replace('|form_columns|', form_columns)
    template = template.replace('|form_fields|', form_fields)
    template = template.replace('|table_headers|', table_headers)
    template = template.replace('|form_field_data|', form_field_data)
    template = template.replace('|model_c_f|', form.model.model_c_f)
    template = template.replace('|model|', form.model.model)
    template = template.replace('|main_params|', main_params)
    template = template.replace('|main_params_and_values|',
                                main_params_and_values)
    template = template.replace('|main_values|', main_values)
    template = template.replace('|model_fields|', model_fields)
    if form.type_ == 'component':
        template = template.replace('|update_component_meta_info|',
                                    update_component_meta_info)
        template = template.replace('|create_component_meta_info|',
                                    create_component_meta_info)
        template = template.replace('|component_meta_info_query|',
                                    component_meta_info_query)
        template = template.replace('|manufacturers_query|', manufacturers_query)
        template = template.replace('|warrantys_query|', warrantys_query)
    else:
        template = template.replace('|update_component_meta_info|',
                                    '')
        template = template.replace('|create_component_meta_info|',
                                    '')
        template = template.replace('|component_meta_info_query|',
                                    '')
        template = template.replace('|manufacturers_query|', '')
        template = template.replace('|warrantys_query|', '')

    with open('{}.vue'.format(form.model.model), 'w') as file:
        file.write(template)
