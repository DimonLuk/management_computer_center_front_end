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
                'input_type': 'select',
                'select_source': "['mATX','ATX','lATX']",
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
    },
    {
        'model': 'processor',
        'type': 'component',
        'fields': (
            {
                'source': 'cores',
                'translation': 'Ядра',
                'input_type': 'text',
                'default': '0',
                'mask': '##',
                'field_type': 'Int'
            },
            {
                'source': 'l1Cache',
                'translation': 'Кэш 1-го уровня(Kb)',
                'input_type': 'text',
                'default': '0',
                'mask': '######',
                'field_type': 'Int'
            },
            {
                'source': 'l2Cache',
                'translation': 'Кэш 2-го уровня(Kb)',
                'input_type': 'text',
                'default': '0',
                'mask': '######',
                'field_type': 'Int'
            },
            {
                'source': 'l3Cache',
                'translation': 'Кэш 3-го уровня(Kb)',
                'input_type': 'text',
                'default': '0',
                'mask': '######',
                'field_type': 'Int'
            },
        )
    },
    {
        'model': 'ram',
        'type': 'component',
        'fields': (
            {
                'source': 'capacity',
                'translation': 'Объём (Gb)',
                'input_type': 'text',
                'default': '',
                'field_type': 'Int',
                'mask': '##'
            },
            {
                'source': 'frequency',
                'translation': 'Частота (MHz)',
                'input_type': 'text',
                'default': '',
                'field_type': 'Int',
                'mask': '####'
            }
        )
    },
    {
        'model': 'trunk',
        'type': 'component',
        'fields': (
            {
                'source': 'width',
                'translation': 'Ширина (см)',
                'input_type': 'text',
                'default': '',
                'field_type': 'Int',
                'mask': '###'
            },
            {
                'source': 'height',
                'translation': 'Высота (см)',
                'input_type': 'text',
                'default': '',
                'field_type': 'Int',
                'mask': '###'
            },
            {
                'source': 'formFactor',
                'translation': 'Форм-фактор',
                'input_type': 'select',
                'select_source': "['mATX','ATX','lATX']",
                'default': '',
                'field_type': 'String',
            }
        )
    },
    {
        'model': 'manufacturer',
        'type': 'not_component',
        'fields': (
            {
                'source': 'title',
                'translation': 'Название',
                'input_type': 'text',
                'default': '',
                'field_type': 'String',
            },
            {
                'source': 'address',
                'translation': 'Адресс',
                'input_type': 'text',
                'default': '',
                'field_type': 'String',
            },
            {
                'source': 'phoneNumber',
                'translation': 'Номер Телефона',
                'input_type': 'text',
                'default': '',
                'field_type': 'String',
                'mask': '+############'
            },
        ),
    },
    {
        'model': 'computer',
        'type': 'computer',
        'fields': (
            {
                'source': 'room',
                'translation': 'Комната',
                'input_type': 'text',
                'default': '',
                'field_type': 'String',
            },
            {
                'source': 'trunkId',
                'translation': 'Корпус',
                'input_type': 'select',
                'default': '',
                'field_type': 'Int',
                'item_text_field': 'combineComponent',
                'item_value_field': 'id',
                'select_source': 'trunks',
            },
            {
                'source': 'motherboardId',
                'translation': 'Материнская плата',
                'input_type': 'select',
                'default': '',
                'field_type': 'Int',
                'item_text_field': 'combineComponent',
                'item_value_field': 'id',
                'select_source': 'motherboards',
            },
            {
                'source': 'ramId',
                'translation': 'Оперативная память',
                'input_type': 'select',
                'default': '',
                'field_type': 'Int',
                'item_text_field': 'combineComponent',
                'item_value_field': 'id',
                'select_source': 'rams',
            },
            {
                'source': 'processorId',
                'translation': 'Процессор',
                'input_type': 'select',
                'default': '',
                'field_type': 'Int',
                'item_text_field': 'combineComponent',
                'item_value_field': 'id',
                'select_source': 'processors',
            },
        )
    }
)
