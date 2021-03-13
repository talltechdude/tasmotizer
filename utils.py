BINS_URL = 'http://ota.tasmota.com'

MODULES = {
    "0": "Custom Template",
    "1": "Sonoff Basic",
    "2": "Sonoff RF",
    "4": "Sonoff TH",
    "5": "Sonoff Dual",
    "39": "Sonoff Dual R2",
    "6": "Sonoff Pow",
    "43": "Sonoff Pow R2",
    "7": "Sonoff 4CH",
    "23": "Sonoff 4CH Pro",
    "41": "Sonoff S31",
    "8": "Sonoff S2X",
    "10": "Sonoff Touch",
    "28": "Sonoff T1 1CH",
    "29": "Sonoff T1 2CH",
    "30": "Sonoff T1 3CH",
    "11": "Sonoff LED",
    "22": "Sonoff BN-SZ",
    "70": "Sonoff L1",
    "26": "Sonoff B1",
    "9": "Slampher",
    "21": "Sonoff SC",
    "44": "Sonoff iFan02",
    "71": "Sonoff iFan03",
    "25": "Sonoff Bridge",
    "3": "Sonoff SV",
    "19": "Sonoff Dev",
    "12": "1 Channel",
    "13": "4 Channel",
    "14": "Motor C/AC",
    "15": "ElectroDragon",
    "16": "EXS Relay(s)",
    "31": "Supla Espablo",
    "35": "Luani HVIO",
    "33": "Yunshan Relay",
    "17": "WiOn",
    "46": "Shelly 1",
    "47": "Shelly 2",
    "45": "BlitzWolf SHP",
    "52": "Teckin",
    "59": "Teckin US",
    "53": "AplicWDP303075",
    "55": "Gosund SP1 v23",
    "65": "Luminea ZX2820",
    "57": "SK03 Outdoor",
    "63": "Digoo DG-SP202",
    "64": "KA10",
    "67": "SP10",
    "68": "WAGA CHCZ02MB",
    "49": "Neo Coolcam",
    "51": "OBI Socket",
    "61": "OBI Socket 2",
    "60": "Manzoku strip",
    "50": "ESP Switch",
    "54": "Tuya MCU",
    "56": "ARMTR Dimmer",
    "58": "PS-16-DZ",
    "20": "H801",
    "34": "MagicHome",
    "37": "Arilux LC01",
    "40": "Arilux LC06",
    "38": "Arilux LC11",
    "42": "Zengge WF017",
    "24": "Huafan SS",
    "36": "KMC 70011",
    "27": "AiLight",
    "48": "Xiaomi Philips",
    "69": "SYF05",
    "62": "YTF IR Bridge",
    "32": "Witty Cloud",
    "18": "Generic"
}

class Aborted(Exception):
    pass


class MissingDetail(Exception):
    pass


class NoBinFile(Exception):
    pass


class NetworkError(Exception):
    pass
