from __future__ import annotations
from argparse import ArgumentParser


SIMPLE_MACROS = {
    # Image: Basic formatting (see wiki)
    'Image': '[Image](?{{Image URL}}.jpg)',
    # Initiative: Basic macros (see wiki)
    'Initiative': '%{{{character}|npc_init}}',
    # Skill check: https://app.roll20.net/forum/post/5591526/5e-ogl-universal-skill-check-macro-updated-for-v2-dot-0
    # By Craig
    'Skill-check': '@{{{character}|wtype}}&{{template:simple}} @{{{character}|rtype}}?{{Skill |Acrobatics,+[[(@{{{character}|acrobatics_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_acrobatics}}*@{{{character}|npc}})]][ACRO] ]]&#125;&#125; {{{{rname=^{{acrobatics-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|acrobatics_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_acrobatics}}*@{{{character}|npc}})]][ACRO] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|acrobatics_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_acrobatics}}*@{{{character}|npc}})]][ACRO] ]] |Animal Handling,+[[(@{{{character}|animal_handling_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_animal_handling}}*@{{{character}|npc}})]][ANIM] ]]&#125;&#125; {{{{rname=^{{animal_handling-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|animal_handling_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_animal_handling}}*@{{{character}|npc}})]][ANIM] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|animal_handling_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_animal_handling}}*@{{{character}|npc}})]][ANIM] ]] |Arcana,+[[(@{{{character}|arcana_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_arcana}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{arcana-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|arcana_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_arcana}}*@{{{character}|npc}})]][ARCA] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|arcana_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_arcana}}*@{{{character}|npc}})]][ARCA] ]] |Athletics,+[[(@{{{character}|athletics_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_athletics}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{athletics-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|athletics_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_athletics}}*@{{{character}|npc}})]][ATHL] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|athletics_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_athletics}}*@{{{character}|npc}})]][ATHL] ]] |Deception,+[[(@{{{character}|deception_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_deception}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{deception-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|deception_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_deception}}*@{{{character}|npc}})]][DECE] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|deception_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_deception}}*@{{{character}|npc}})]][DECE] ]] |History,+[[(@{{{character}|history_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_history}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{history-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|history_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_history}}*@{{{character}|npc}})]][HIST] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|history_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_history}}*@{{{character}|npc}})]][HIST] ]] |Insight,+[[(@{{{character}|insight_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_insight}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{insight-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|insight_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_insight}}*@{{{character}|npc}})]][INSI] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|insight_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_insight}}*@{{{character}|npc}})]][INSI] ]] |Intimidation,+[[(@{{{character}|intimidation_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_intimidation}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{intimidation-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|intimidation_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_intimidation}}*@{{{character}|npc}})]][INTI] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|intimidation_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_intimidation}}*@{{{character}|npc}})]][INTI] ]] |Investigation,+[[(@{{{character}|investigation_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_investigation}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{investigation-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|investigation_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_investigation}}*@{{{character}|npc}})]][INVE] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|investigation_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_investigation}}*@{{{character}|npc}})]][INVE] ]] |Medicine,+[[(@{{{character}|medicine_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_medicine}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{medicine-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|medicine_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_medicine}}*@{{{character}|npc}})]][MEDI] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|medicine_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_medicine}}*@{{{character}|npc}})]][MEDI] ]] |Nature,+[[(@{{{character}|nature_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_nature}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{nature-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|nature_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_nature}}*@{{{character}|npc}})]][NATU] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|nature_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_nature}}*@{{{character}|npc}})]][NATU] ]] |Perception,+[[(@{{{character}|perception_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_perception}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{perception-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|perception_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_perception}}*@{{{character}|npc}})]][PERC] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|perception_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_perception}}*@{{{character}|npc}})]][PERC] ]] |Performance,+[[(@{{{character}|performance_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_performance}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{performance-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|performance_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_performance}}*@{{{character}|npc}})]][PERF] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|performance_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_performance}}*@{{{character}|npc}})]][PERF] ]] |Persuasion,+[[(@{{{character}|persuasion_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_persuasion}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{persuasion-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|persuasion_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_persuasion}}*@{{{character}|npc}})]][PERS] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|persuasion_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_persuasion}}*@{{{character}|npc}})]][PERS] ]] |Religion,+[[(@{{{character}|religion_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_religion}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{religion-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|religion_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_religion}}*@{{{character}|npc}})]][RELI] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|religion_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_religion}}*@{{{character}|npc}})]][RELI] ]] |Sleight of Hand,+[[(@{{{character}|sleight_of_hand_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_sleight_of_hand}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{sleight_of_hand-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|sleight_of_hand_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_sleight_of_hand}}*@{{{character}|npc}})]][SLEI] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|sleight_of_hand_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_sleight_of_hand}}*@{{{character}|npc}})]][SLEI] ]] |Stealth,+[[(@{{{character}|stealth_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_stealth}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{stealth-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|stealth_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_stealth}}*@{{{character}|npc}})]][STEA] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|stealth_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_stealth}}*@{{{character}|npc}})]][STEA] ]] |Survival,+[[(@{{{character}|survival_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_survival}}*@{{{character}|npc}})]][ARC] ]]&#125;&#125; {{{{rname=^{{survival-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|survival_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_survival}}*@{{{character}|npc}})]][SURV] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|survival_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_survival}}*@{{{character}|npc}})]][SURV] ]] }}}}}} @{{{character}|global_skill_mod}} @{{{character}|charname_output}}',
    # Saving throw: https://app.roll20.net/forum/post/5591512/5e-ogl-universal-saving-throw-macro-updated-for-v2-dot-0
    # By Kyle G. (Original by Craig)
    'Saving-throw': """@{{{character}|wtype}}&{{template:simple}} @{{{character}|rtype}}?{{Save
|Strength,+[[(@{{{character}|strength_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_str_save}}*@{{{character}|npc}})]][STR SAVE] ]]&#125;&#125; {{{{rname=^{{strength-save-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|strength_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_str_save}}*@{{{character}|npc}})]][STR SAVE] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|strength_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_str_save}}*@{{{character}|npc}})]][STR SAVE] ]]
|Dexterity,+[[(@{{{character}|dexterity_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_dex_save}}*@{{{character}|npc}})]][DEX SAVE] ]]&#125;&#125; {{{{rname=^{{dexterity-save-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|dexterity_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_dex_save}}*@{{{character}|npc}})]][DEX SAVE] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|dexterity_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_dex_save}}*@{{{character}|npc}})]][DEX SAVE] ]]
|Constitution,+[[(@{{{character}|constitution_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_con_save}}*@{{{character}|npc}})]][CON SAVE] ]]&#125;&#125; {{{{rname=^{{constitution-save-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|constitution_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_con_save}}*@{{{character}|npc}})]][CON SAVE] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|constitution_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_con_save}}*@{{{character}|npc}})]][CON SAVE] ]]
|Intelligence,+[[(@{{{character}|intelligence_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_int_save}}*@{{{character}|npc}})]][INT SAVE] ]]&#125;&#125; {{{{rname=^{{intelligence-save-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|intelligence_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_int_save}}*@{{{character}|npc}})]][INT SAVE] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|intelligence_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_int_save}}*@{{{character}|npc}})]][INT SAVE] ]]
|Wisdom,+[[(@{{{character}|wisdom_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_wis_save}}*@{{{character}|npc}})]][WIS SAVE] ]]&#125;&#125; {{{{rname=^{{wisdom-save-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|wisdom_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_wis_save}}*@{{{character}|npc}})]][WIS SAVE] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|wisdom_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_wis_save}}*@{{{character}|npc}})]][WIS SAVE] ]]
|Charisma,+[[(@{{{character}|charisma_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_cha_save}}*@{{{character}|npc}})]][CHA SAVE] ]]&#125;&#125; {{{{rname=^{{charisma-save-u&#125;&#125;&#125; {{{{mod=[[ [[(@{{{character}|charisma_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_cha_save}}*@{{{character}|npc}})]][CHA SAVE] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[(@{{{character}|charisma_save_bonus}}@{{{character}|pbd_safe}}*(1-ceil((@{{{character}|npc}})*0.00001)))+(@{{{character}|npc_cha_save}}*@{{{character}|npc}})]][CHA SAVE] ]]
}}}}}} {{{{global=@{{{character}|global_save_mod}}}}}} @{{{character}|charname_output}}""",
    # Ability Check: https://app.roll20.net/forum/post/5591522/5e-ogl-universal-ability-check-macro-updated-for-v2-dot-0
    # By Kyle G. (Original by Craig)
    'Ability-check': '''@{{{character}|wtype}}&{{template:simple}} @{{{character}|rtype}}?{{Stat
|Strength,+[[@{{{character}|strength_mod}}]][STR] ]]&#125;&#125; {{{{rname=^{{strength-u&#125;&#125;&#125; {{{{mod=[[ [[@{{{character}|strength_mod}}]][STR] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[@{{{character}|strength_mod}}]][STR] ]]
|Dexterity,+[[@{{{character}|dexterity_mod}}]][DEX] ]]&#125;&#125; {{{{rname=^{{dexterity-u&#125;&#125;&#125; {{{{mod=[[ [[@{{{character}|dexterity_mod}}]][DEX] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[@{{{character}|dexterity_mod}}]][DEX] ]]
|Constitution,+[[@{{{character}|constitution_mod}}]][CON] ]]&#125;&#125; {{{{rname=^{{constitution-u&#125;&#125;&#125; {{{{mod=[[ [[@{{{character}|constitution_mod}}]][CON] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[@{{{character}|constitution_mod}}]][CON] ]]
|Intelligence,+[[@{{{character}|intelligence_mod}}]][INT] ]]&#125;&#125; {{{{rname=^{{intelligence-u&#125;&#125;&#125; {{{{mod=[[ [[@{{{character}|intelligence_mod}}]][INT] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[@{{{character}|intelligence_mod}}]][INT] ]]
|Wisdom,+[[@{{{character}|wisdom_mod}}]][WIS] ]]&#125;&#125; {{{{rname=^{{wisdom-u&#125;&#125;&#125; {{{{mod=[[ [[@{{{character}|wisdom_mod}}]][WIS] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[@{{{character}|wisdom_mod}}]][WIS] ]]
|Charisma,+[[@{{{character}|charisma_mod}}]][CHA] ]]&#125;&#125; {{{{rname=^{{charisma-u&#125;&#125;&#125; {{{{mod=[[ [[@{{{character}|charisma_mod}}]][CHA] ]]&#125;&#125; {{{{r1=[[@{{{character}|d20}}+[[@{{{character}|charisma_mod}}]][CHA] ]]
}}}}}} {{{{global=@{{{character}|global_skill_mod}}}}}} @{{{character}|charname_output}}''',
}

COMPLEX_MACROS = {
    'Passive-Perception': {
        'base': '{message_target} &{{template:default}} {{{{name=Passive Perception}}}} {characters_parsed_template}',
        'character_template': '{{{{{character_name}  [[@{{{character}|passive_wisdom}}]]}}}}',
    },
    'equipment-weight': {
        'base': '{message_target} &{{template:default}} {{{{name=Equipment weight}}}} {characters_parsed_template}',
        'character_template': '{{{{{character_name}  [[@{{{character}|weighttotal}}]]}}}}',
    },
    'total-weight': {
        'base': '{message_target} &{{template:default}} {{{{name=Total weight}}}} {characters_parsed_template}',
        'character_template': '{{{{{character_name}  [[@{{{character}|weighttotal}}+@{{{character}|weight}}]]}}}}',
    }
}

MACROS = SIMPLE_MACROS.keys() | COMPLEX_MACROS.keys()
    

stroke = '--------------------------------------------------------------------------------'
small_stroke = '----------'

def generate_macros(player: bool, characters: List[str]) -> None:
    print(f'Generating macros for: {"Player" if player else "DM"}')

    if characters:
        print(f'Using characters: {characters}')
    else:
        print('Generating macros for selected tokens')

    print(stroke)
    for macro_name in MACROS:

        if macro_name in SIMPLE_MACROS:
            if not player or not characters:
                generate_simple_macro(macro_name, 'selected', player)

            else:
                for character in characters:
                    generate_simple_macro(macro_name, character, player)
                    if character != characters[-1]:
                        print(small_stroke)

        elif macro_name in COMPLEX_MACROS:
            generate_complex_macro(macro_name, characters, player)

        print(stroke)
        
def generate_simple_macro(macro_name: str, character: str, player: bool) -> None:
    """Print a simple macro for the specified character

    Args:
        macro_name (str): The name (key) of the macro
        character (str): The name of the targeted character
        message_target (str): The target of the message
    """

    message_target = f'/w {character}' if player else '/w gm'
    print(f'{macro_name} for {character}')
    print(small_stroke)
    print(SIMPLE_MACROS[macro_name].format(**locals()))


def generate_complex_macro(macro_name: str, characters: List[str], player: bool) -> None:
    message_target = '/me' if player else '/w gm'
    print(macro_name)
    print(small_stroke)
    
    if characters:
        characters_parsed_template = ' '.join((
            COMPLEX_MACROS[macro_name]['character_template'].format(**locals(), character_name=character)
            for character in characters
        ))
    
    else:
        character = 'selected'
        character_name = '@{selected|character_name}'
        characters_parsed_template = COMPLEX_MACROS[macro_name]['character_template'].format(**locals())

    print(COMPLEX_MACROS[macro_name]['base'].format(**locals()))


if __name__ == '__main__':
    argparser = ArgumentParser()
    argparser.add_argument('-p', '--player', action='store_true', help='Generate only for players')
    argparser.add_argument(
        '-c', '--characters', nargs='+',
        help=(
            'Generate macros for the specified characters. '
            'If not specified it will only generate selected token macros. '
            'Multiple characters can be specified'
        )
    )
    args = argparser.parse_args()

    generate_macros(player=args.player, characters=args.characters or [])
