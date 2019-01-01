EXCLUDED_FROM_COMPONENTS = (
    'serialNumber',
    'warrantyId',
    'manufacturerId',
    'status'
)


update_component_meta_info = """
      let componentMetaInfoId;
      componentMetaInfoId = await this.$apollo.mutate({
        mutation: gql`
          mutation($id: Int!, $manufacturerId: Int!, $warrantyId: Int!, $status: String!, $serialNumber: String!) {
            updateComponentmetainfo(input : {
              id: $id
              manufacturerId: $manufacturerId,
              warrantyId: $warrantyId,
              status: $status,
              serialNumber: $serialNumber
            }) {
              componentmetainfo {
                id
              }
            }
          }
        `,
        variables: {
          id: Number(data.componentMetaInfoId),
          manufacturerId: Number(this.formData.manufacturerId),
          warrantyId: Number(this.formData.warrantyId),
          status: this.formData.status,
          serialNumber: this.formData.serialNumber,
        }
      })
      componentMetaInfoId = componentMetaInfoId.data.updateComponentmetainfo.componentmetainfo.id;
"""


create_component_meta_info = """
      let componentMetaInfoId;
      componentMetaInfoId = await this.$apollo.mutate({
        mutation: gql`
          mutation($manufacturerId: Int!, $warrantyId: Int!, $status: String!, $serialNumber: String!) {
            createComponentmetainfo(input : {
              manufacturerId: $manufacturerId,
              warrantyId: $warrantyId,
              status: $status,
              serialNumber: $serialNumber
            }) {
              componentmetainfo {
                id
              }
            }
          }
        `,
        variables: {
          manufacturerId: Number(this.formData.manufacturerId),
          warrantyId: Number(this.formData.warrantyId),
          status: this.formData.status,
          serialNumber: this.formData.serialNumber,
        }
      })
      componentMetaInfoId = componentMetaInfoId.data.createComponentmetainfo.componentmetainfo.id;
"""


manufacturers_query = """
    manufacturers: gql`
      query {
        manufacturers {
          id,
          title
        }
      }
    `,
"""


warrantys_query = """
    warrantys: gql`
      query {
        warrantys {
          id,
          startDate,
          endDate
        }
      }
    `,
"""

component_meta_info_query = """
          componentMetaInfo {
            serialNumber,
            manufacturerId,
            warrantyId,
            status
          }
"""


def generate_form_columns(fields):
    template = \
        """
        <td class='text-xs-right'>{{{{ props.item.{source} }}}}</td>"""
    result = ''
    for field in fields:
        result += template.format(source=field.source)
    return result


def generate_form_fields(fields):
    result = ''
    for field in fields:
        tmp = ''
        if field.input_type == 'text':
            tmp += '<v-text-field\n'
            tmp += '  :rules="rules.notMoreThanTen"\n'
            if field.mask:
                tmp += '  mask="{mask}"\n'.format(mask=field.mask)
        elif field.input_type == 'select':
            tmp += '<v-select\n'
            tmp += '  :items="{select_source}"\n'.format(
                select_source=field.select_source
            )
            tmp += '  solo\n'
            tmp += '  :rules="rules.notEmptySelector"\n'
            if field.item_text_field:
                tmp += '  item-text="{item_text_field}"\n'.format(
                    item_text_field=field.item_text_field
                )
            if field.item_value_field:
                tmp += '  item-value="{item_value_field}"\n'.format(
                    item_value_field=field.item_value_field
                )

        tmp += '  v-model="formData.{flat_name}"\n'.format(
            flat_name=field.flat_name
        )
        tmp += '  label="{translation}"\n'.format(
            translation=field.translation
        )
        tmp += '  required\n'
        tmp += '  v-if=\'mode === "create" || mode === "update"\'\n'
        tmp += '>'
        if field.input_type == 'text':
            tmp += '</v-text-field>\n'
        elif field.input_type == 'select':
            tmp += '</v-select>\n'
        result += tmp
    return result


def generate_table_headers(fields):
    result = ''
    template = \
        """
    {{ text: '{translation}', align: 'right', value: '{source}' }},"""
    for field in fields:
        result += template.format(
            translation=field.translation,
            source=field.source
        )
    return result


def generate_form_fields_data(fields):
    result = ''
    template = \
        """
    {flat_name}: '{default}',"""
    for field in fields:
        result += template.format(
            flat_name=field.flat_name,
            default=field.default
        )
    return result


def generate_main_params(fields, form_type):
    result = ''
    template = '${flat_name}: {graphql_type}, '
    for field in fields:
        if form_type == 'component' and field.flat_name not in \
                EXCLUDED_FROM_COMPONENTS:
            result += template.format(
                flat_name=field.flat_name,
                graphql_type=field.graphql_type
            )
        elif form_type != 'component':
            result += template.format(
                flat_name=field.flat_name,
                graphql_type=field.graphql_type
            )
    if form_type == 'component':
        result += template.format(flat_name='componentMetaInfoId',
                                 graphql_type='Int!')
    return result[:-2]


def generate_main_params_and_values(fields, form_type):
    result = ''
    template = '{flat_name}: ${flat_name},\n'
    for field in fields:
        if form_type == 'component' and field.flat_name not in \
                EXCLUDED_FROM_COMPONENTS:
            result += template.format(
                flat_name=field.flat_name
            )
        elif form_type != 'component':
            result += template.format(
                flat_name=field.flat_name
            )
    if form_type == 'component':
        result += template.format(flat_name='componentMetaInfoId')
    return result[:-2]


def generate_main_values(fields, form_type):
    result = ''
    pre_template = 'this.formData.{flat_name}'
    template = '{flat_name}: {pre_value},\n'
    for field in fields:
        if form_type == 'component' and field.flat_name not in \
                EXCLUDED_FROM_COMPONENTS:
            pre_value = field.typed.format(pre_template)
            pre_value = pre_value.format(flat_name=field.flat_name)
            result += template.format(
                flat_name=field.flat_name,
                pre_value=pre_value
            )
        elif form_type != 'component':
            pre_value = field.typed.format(pre_template)
            pre_value = pre_value.format(flat_name=field.flat_name)
            result += template.format(
                flat_name=field.flat_name,
                pre_value=pre_value
            )
    if form_type == 'component':
        result += template.format(
            flat_name='componentMetaInfoId',
            pre_value='Number(componentMetaInfoId)'
        )
    return result[:-2]


def generate_model_fields(fields, form_type):
    result = ''
    template = '{flat_name},\n'
    for field in fields:
        if field.flat_name not in EXCLUDED_FROM_COMPONENTS:
            result += template.format(
                flat_name=field.flat_name
            )
    if form_type == 'component':
        result += template.format(flat_name='componentMetaInfoId')
    return result[:-2]
