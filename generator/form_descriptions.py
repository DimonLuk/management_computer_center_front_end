COMPONENT_DEFAULTS = (
    {
        'source': 'componentMetaInfo.serialNumber',
        'translation': 'Серийный номер',
        'input_type': 'text',
        'mask': 'NNNNNNNNNN', 'default': '',
        'field_type': 'String',
    },
    {
        'source': 'componentMetaInfo.manufacturerId',
        'translation': 'Производитель',
        'input_type': 'select',
        'item_text_field': 'title',
        'item_value_field': 'id',
        'select_source': 'manufacturers',
        'default': '',
        'field_type': 'Int',
    },
    {
        'source': 'componentMetaInfo.warrantyId',
        'translation': 'Гарантия',
        'input_type': 'select',
        'item_text_field': 'combineDates',
        'item_value_field': 'id',
        'select_source': 'warrantys',
        'default': '',
        'field_type': 'Int',
    },
    {
        'source': 'componentMetaInfo.status',
        'translation': 'Статус',
        'input_type': 'select',
        'select_source': "['Ready','Working','Broken','Reparing','Repared']",
        'default': '',
        'field_type': 'String',
    },
)


FORMS = (
    {
        'model': 'motherboard',
        'type': 'component',
        'fields': (
            {
                'source': 'formFactor',
                'translation': 'Форм-фактор',
                'input_type': 'text',
                'default': '',
                'field_type': 'String',
            },
            {
                'source': 'chipset',
                'translation': 'Чипсет',
                'input_type': 'text',
                'default': '',
                'field_type': 'String',
            },
            {
                'source': 'pciSlots',
                'translation': 'PCI-слоты',
                'input_type': 'text',
                'default': '',
                'mask': '##',
                'field_type': 'Int',
            },
            {
                'source': 'usedPciSlots',
                'translation': 'Занятые PCI-слоты',
                'input_type': 'text',
                'default': '0',
                'mask': '##',
                'field_type': 'Int',
            },
            {
                'source': 'ramSlots',
                'translation': 'Слоты RAM',
                'input_type': 'text',
                'default': '',
                'mask': '##',
                'field_type': 'Int',
            },
            {
                'source': 'usedRamSlots',
                'translation': 'Занятыe слоты RAM',
                'input_type': 'text',
                'default': '0',
                'mask': '##',
                'field_type': 'Int',
            },
        ),
    },
    {
        'model': 'warranty',
        'type': 'not_component',
        'fields': (
            {
                'source': 'startDate',
                'translation': 'Дата начала',
                'input_type': 'text',
                'default': '',
                'mask': '####-##-##',
                'field_type': 'Date',
            },
            {
                'source': 'endDate',
                'translation': 'Дата конца',
                'input_type': 'text',
                'default': '',
                'mask': '####-##-##',
                'field_type': 'Date',
            }
        ),
    }
)
