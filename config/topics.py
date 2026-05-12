from .aliases import *
from .pools import *


TOPICS = {
    "turkey_politics": {"liders": TURKEY["liders"]},
    "turkey_security": {"security": TURKEY["security"]},
    "turkey_economy": {"economy": TURKEY["economy"]},
    "middle_east": {"middle_east": MIDDLE_EAST},
    "nato": {"nato": NATO},
    "wars_conflicts": {"war": WARS},
    "turkey_us_relations": {"us_relations": RELATIONS["usa"]},
    "turkey_greece_relations": {"gr_relations": RELATIONS["greece"]},
    "turkey_military_technology": {"military_tech": TURKEY["military_tech"]},
    "major_global_events": {"globe": GLOBAL_EVENTS},
    "migration": {"migration": TURKEY["migration"]},
}


# print(TOPICS)