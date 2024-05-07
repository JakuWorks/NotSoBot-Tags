import random
import dataclasses


@dataclasses.dataclass
class emoji:
    LENNY_FACE: str = "( ͡° ͜ʖ ͡°)"
    ANGEL: str = ":angel:"
    WOMAN_FAIRY: str = ":woman_fairy:"
    CROWN: str = ":crown:"
    FACE_VOMITING: str = ":face_vomiting:"
    MAGE_MAN_BLUE: str = ":mage:"
    MAGE_MAN_RED: str = ":man_mage:"
    YOU_ARE_THE_STONEPOCALYPSE: str = "ɎØᵾ ȺɌɆ ŦĦɆ **SŦØNɆⱣØȻȺŁɎⱣSɆ**"
    BABY: str = ":baby:"
    ALIEN: str = ":alien:"
    FLYING_SAUCER: str = ":flying_saucer:"
    PINK_HEART: str = ":pink_heart:"
    MONKEY: str = ":monkey:"
    MONKEY_FACE: str = ":monkey_face:"
    BEE: str = ":bee:"
    WORM: str = ":worm:"
    SUPERHERO: str = ":superhero:"
    SMILING_IMP: str = ":smiling_imp:"
    FACE_WITH_OPEN_EYES_AND_HAND_OVER_MOUTH = ":face_with_open_eyes_and_hand_over_mouth:"
    NERD: str = ":nerd:"
    DISGUISED_FACE: str = ":disguised_face:"
    WING: str = ":wing:"
    ZAP: str = ":zap:"
    NINJA: str = ":ninja:"
    JAPANESE_GOBLIN: str = ":japanese_goblin:"
    JAPANESE_OGRE: str = ":japanese_ogre:"
    FIRE: str = ":fire:"
    TROLL: str = ":troll:"
    ROBOT: str = ":robot:"
    HAROLD: str = ":harold:"
    BLACK_JOKER: str = ":black_joker:"


def main():
    min: int = -1
    max: int = 101
    include_min: bool = True
    include_max: bool = True

    comments: dict[int, str] = {
        -1 : "You are stonekind's biggest mistake...",
        0 : "You have failed your role as a stoneman...",
        1 : f"You are a stonekisser ewwwww {emoji.FACE_VOMITING}",
        2 : "You are a stone Warrior! WAIT... Breaking News: You've been kidnapped by the Stonemen! You are now a mere shell of the warrior you've been... You are a depressed pebble",
        3 : f"You are what appears like stone dust",
        4 : f"You are a stone worm {emoji.WORM}",
        5 : "You are a grain of sand",
        6 : "You are two grains of sand",
        7 : "You are a tiny little pebble!",
        8 : "You are a tiny pebble",
        9 : "You are two tiny pebbles",
        10 : "You are a small pebble",
        11 : "You are two small pebbles",
        12 : "You are a beginner pebbleman",
        13 : "You are a pebbleman",
        14 : f"You are a stone factory worker {emoji.HAROLD}",
        15 : "You are a small rock",
        16 : "You are two small rocks",
        17 : "You are a common rock",
        18 : "You are a larger rock",
        19 : f"You have a big rock {emoji.LENNY_FACE}",
        20 : "You are a rookie rockman",
        21 : "You are a beginner rockman",
        22 : "You are a rockman!",
        23 : f"You are a stone newborn. {emoji.BABY}. You are adorable! {emoji.PINK_HEART}",
        24 : "You are a young stone",
        25 : f"You are a stone jester {emoji.BLACK_JOKER}",
        26 : "You are a stone",
        27 : "You are a warrior stone",
        28 : "You are a wise elder stone",
        29 : f"WHAT!? You are a Stone Bee??!! {emoji.BEE}",
        30 : "What the fuck!!! You are a stone tree!!!!!????",
        31 : "You are a stone enthusiast",
        32 : f"You are a stone nerd {emoji.NERD}",
        33 : f"It appears you are a stone monkey! {emoji.MONKEY}{emoji.MONKEY_FACE}",
        34 : f"You are the giga stone nerd! {emoji.DISGUISED_FACE}",
        35 : f"You are stonaholic!",
        36 : "You are a rookie stoneman",
        37 : "You are two rookie stonemen?",
        38 : "You are a beginner stoneman",
        39 : "STONEWOMAN!!!???",
        40 : "You are a stoneman apprentice",
        41 : "You are a warrior stoneman",
        42 : "You are a popular stoneman warrior",
        43 : "You are a small stoneman leader",
        44 : "You are a chief stoneman",
        45 : "You are the wise elder stoneman",
        46 : "You are a stone broodmother!",
        47 : "STONEMAN!!!",
        48 : "You throw Boulders. But you have't earned your boulderman title yet",
        49 : "You are a Boulderman!",
        50 : "You are two Bouldermen?!",
        51 : "You are a Stone Priest!",
        52 : f"You are Rock-Hard {emoji.LENNY_FACE}",
        53 : "You are Big Boulderman",
        54 : "You are a Big Buff Boulderman",
        55 : "You are a Big Boulderman Warrior!",
        56 : "You are a Famous Boulderman Warrior!",
        57 : "You are a Boulderman Knight!",
        58 : "You are a Famous Boulderman Knight!",
        59 : f"You are a Stone Ninja! {emoji.NINJA}",
        60 : f"You are a Stone Robot! {emoji.ROBOT} How!??!??!?",
        61 : f"You are a stone Witch!",
        62 : f"You are a Grandmaster Stone Ninja!!",
        63 : f"You are a Supreme Grandmaster Stone Ninja!!!",
        64 : f"You are a Stone Wizard Apprentice! {emoji.MAGE_MAN_BLUE}",
        65 : f"You are a Beginner Stone Spellcaster! {emoji.MAGE_MAN_BLUE}",
        66 : f"You are a Stone Wizard! {emoji.MAGE_MAN_RED}",
        67 : f"You are a Stone Sorcerer! A Stonecerer!!! {emoji.MAGE_MAN_RED}",
        68 : f"You are the Stone Archwizard!!!",
        69 : f"You have a Big Stone {emoji.LENNY_FACE}",
        70 : f"You are beautiful stone Fairy? {emoji.WOMAN_FAIRY}",
        71 : f"You are the Stone Superhero! {emoji.SUPERHERO}",
        72 : f"You are a stone GIANT {emoji.TROLL}",
        73 : "You are an Allah's Warrior! Stone these goddamn Boykissers!!!",
        74 : "You are the Allah's Knight! Stone those goddamn Boykissers!!!",
        75 : f"You are a stone Alien?! {emoji.ALIEN} {emoji.FLYING_SAUCER}",
        76 : "You are a Stone Aliens Leader!",
        77 : "You are the Prince of the Stone Aliens!",
        78 : f"You are the King Of the Stone Aliens! {emoji.CROWN}",
        79 : "You are the Pebble QUEEN!",
        80 : "You are the Pebble KING!",
        81 : "You are the Rock QUEEN!",
        82 : "You are the Rock KING!",
        83 : "You are the Stone QUEEN!",
        84 : "You are the Stone KING!",
        85 : "You are the BOULDER KING!",
        86 : "You are the POPE of Stonekind!",
        87 : "You are a Stone **TITAN**!!!",
        88 : f"You are the Supreme Boulder EMPEROR!! THE LORD OF STONES!!!! {emoji.CROWN}",
        89 : f"You are a Baby Stone Angel! {emoji.ANGEL}",
        90 : f"You are a Stone Imp! {emoji.JAPANESE_GOBLIN}",
        91 : f"You are a hot stone Succubus! {emoji.LENNY_FACE}",
        92 : f"You are a Stone Demon! {emoji.JAPANESE_OGRE}",
        93 : f"You are a Stone Angel! {emoji.ANGEL}",
        94 : f"You are a Stone Archdemon! {emoji.FIRE}{emoji.JAPANESE_OGRE}{emoji.FIRE}",
        95 : f"You are a Stone Archangel! {emoji.WING}",
        96 : "You are a Lesser Stone Idol!",
        97 : "You are a Stone Deity!",
        98 : f"You are the Stone Zeus! {emoji.ZAP}",
        99 : f"{emoji.FACE_WITH_OPEN_EYES_AND_HAND_OVER_MOUTH} **You are the stone Devil!** {emoji.SMILING_IMP} *you may not be good but you sure are powerful*",
        100 : f"**You are the stone GOD**",
        101 : f"{emoji.YOU_ARE_THE_STONEPOCALYPSE}",
    }

    if not include_min:
        min = min + 1
    if not include_max:
        max = max - 1

    if min > max:
        raise RuntimeError("Minimum stone count cannot be greater than maximum!")

    stone_count = random.randint(min, max)

    comment_raw: str = comments[stone_count]
    comment_formatted: str = f"*{stone_count}* {comment_raw}"

    print(comment_formatted)


main()
