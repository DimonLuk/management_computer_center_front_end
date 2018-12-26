from form_descriptions import COMPONENT_DEFAULTS, FORMS # NOQA


class FieldInfo:
    def __init__(
        self,
        source=None,
        default=None,
        input_type=None,
        field_type=None,
        translation=None,
        item_text_field=None,
        item_value_field=None,
        select_source=None,
        mask=None,
    ):
        if source and default is not None and input_type and field_type:
            self.source = source
            self.default = default
            self.input_type = input_type
            self.field_type = field_type
            self.item_text_field = item_text_field
            self.item_value_field = item_value_field
            self.mask = mask
            if '.' in self.source:
                self.flat_name = self.source.split('.')[-1]
            else:
                self.flat_name = self.source
            self.translation = translation if translation else self.flat_name
            if self.field_type == 'Int':
                self.typed = 'Number({})'
                self.typed_source = 'Number({})'.format(self.source)
                self.graphql_type = '{}!'.format(self.field_type)
            else:
                self.typed = '{}'
                self.typed_source = '{}'.format(self.source)
                self.graphql_type = '{}!'.format(self.field_type)
            self.select_source = select_source
        else:
            raise Exception('source, default, input_type and '
                            'field_type are requried')


class ModelInfo:
    def __init__(
        self,
        name=None
    ):
        if name:
            self._name = name.lower()
            self.model = self._name
            self.model_s = '{}s'.format(self.model)
            self.model_c_f = '{}{}'.format(self.model[0].upper(),
                                           self.model[1:])
        else:
            raise Exception('Provide name')


class Form:
    def __init__(self, obj):
        self.model = ModelInfo(name=obj.get('model'))
        self.fields = []
        self.type_ = obj.get('type')
        if obj.get('type') == 'component':
            for field in COMPONENT_DEFAULTS:
                self.fields.append(FieldInfo(**field))
        for field in obj.get('fields'):
            self.fields.append(FieldInfo(**field))
