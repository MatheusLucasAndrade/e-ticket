from enum import Enum

class UrgencyProtocol(Enum):
    LOW = 'Baixo'
    MEDIUM = 'Médio'
    HIGH = 'Alto'

class PreferenceCategory(Enum):
    ELDERLY = "Idoso"
    PREGNANT = "Amamentando"
    DISABILITY = "Deficiente"
    MOBILITY_REDUCTION = "Mobilidade_reduzida"
    LACTATING = "Lactante"
    INFANT_IN_ARMS = "Criança_de_colo"
    NO_PREFERENCE = "Sem_preferencia"
