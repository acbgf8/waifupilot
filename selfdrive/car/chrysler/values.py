from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu


class CarControllerParams:
  STEER_STEP = 1          # LKAS steering commands sent at 100Hz
  HUD_STEP = 25           # HUD updates sent at 4Hz

  STEER_MAX = 306        # Observed factory LKAS hitting 306, we may have even more headroom here
  STEER_DELTA_UP = 5      # Factory LKAS ramps up at 5 per ms, have not tested more
  STEER_DELTA_DOWN = 5    # Factory LKAS ramps down at 5 per ms, have not tested more, more is probably possible
  STEER_ERROR_MAX = 80    # FIXME: is this actually needed/usable for anything besides Toyota?
  STEER_DRIVER_ALLOWANCE = 80
  STEER_DRIVER_MULTIPLIER = 3    # weight driver torque heavily
  STEER_DRIVER_FACTOR = 1        # from dbc



class CAR:

  JEEP_CHEROKEE_SRT_2014 = "JEEP GRAND CHEROKEE SRT 2014"
  CHRYSLER_200_V6 = "CHRYSLER 200 V6 2016"
  KL_CHEROKEE = "2014-2018 CHEROKEE"

FINGERPRINTS = {
  CAR.JEEP_CHEROKEE_SRT_2014: [
    {256: 4, 257: 5, 258: 8, 264: 8, 268: 8, 272: 6, 273: 6, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 292: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 352: 8, 362: 8, 368: 8, 376: 3, 384: 8, 388: 4, 416: 7, 448: 6, 456: 4, 464: 8, 500: 8, 501: 8, 512: 8, 514: 8, 520: 8, 532: 8, 536: 8, 544: 8, 557: 8, 559: 8, 560: 4, 564: 4, 571: 3, 584: 8, 608: 8, 618: 8, 624: 8, 625: 8, 632: 8, 639: 8, 658: 6, 660: 8, 671: 8, 672: 8, 678: 8, 680: 8, 683: 8, 684: 8, 685: 8, 703: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 729: 5, 736: 8, 737: 8, 746: 5, 752: 2, 760: 8, 761: 8, 762: 5, 764: 8, 766: 8, 772: 8, 773: 8, 776: 8, 779: 8, 783: 8, 784: 8, 792: 8, 799: 8, 800: 8, 804: 8, 806: 2, 808: 8, 810: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 831: 6, 832: 8, 836: 2, 838: 2, 844: 5, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 874: 2, 882: 8, 897: 8, 924: 3, 937: 8, 947: 8, 948: 8, 956: 8, 968: 8, 969: 4, 970: 8, 974: 5, 975: 8, 977: 4, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 994: 3, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1027: 8, 1031: 8, 1033: 8, 1050: 8, 1058: 8, 1059: 8, 1062: 8, 1098: 8, 1100: 8, 1216: 8, 1218: 8, 1220: 8, 1223: 8, 1225: 8, 1227: 8, 1242: 8, 1250: 8, 1251: 8, 1252: 8, 1264: 8, 1408: 8, 1572: 8, 1856: 8, 1858: 8, 1860: 8, 1863: 8, 1865: 8, 1867: 8, 1882: 8, 1890: 8, 1891: 8, 1892: 8, 1898: 8, 1899: 8, 1900: 8, 1902: 8, 1904: 8, 2017: 8, 2019: 8, 2023: 8, 2025: 8},
  ],
  CAR.CHRYSLER_200_V6: [
    {242: 7, 244: 7, 247: 8, 253: 6, 254: 4, 480: 8, 482: 8, 484: 8, 486: 8, 488: 5, 490: 4, 492: 8, 494: 6, 496: 8, 498: 8, 500: 7, 502: 4, 504: 8, 508: 8, 510: 5, 512: 8, 514: 5, 514: 8, 520: 7, 521: 8, 522: 4, 524: 4, 738: 8, 740: 8, 742: 8, 744: 8, 746: 5, 748: 8, 750: 3, 751: 1, 752: 8, 754: 8, 756: 5, 758: 1, 760: 5, 762: 3, 875: 8, 994: 4, 996: 6, 998: 5, 1002: 8, 1004: 8, 1006: 7, 1006: 8, 1232: 8, 1236: 8, 1238: 4, 1240: 8, 1242: 8, 1244: 8, 1246: 8, 1248: 8, 1250: 8, 1252: 8, 1254: 2, 1256: 2, 1258: 8, 1260: 8, 1262: 8, 1264: 7, 1266: 5, 1268: 8, 1375: 8, 1492: 4, 1494: 4, 1496: 6, 1498: 2, 1500: 4, 1502: 8, 1504: 7, 1508: 8, 1510: 8, 1625: 4, 1627: 1, 1746: 1, 1752: 2, 1754: 4, 1756: 4, 1992: 8, 1993: 8, 1994: 2, 1996: 2, 1999: 5, 2000: 8, 2002: 2, 2004: 8, 2006: 3, 2008: 4, 2010: 7},
  ],  
  CAR.KL_CHEROKEE: [
    {242: 7, 244: 7, 247: 8, 253: 6, 254: 4, 480: 8, 482: 8, 484: 8, 486: 8, 488: 5, 490: 4, 492: 8, 494: 6, 496: 8, 498: 8, 500: 7, 502: 4, 504: 8, 508: 8, 510: 5, 512: 8, 514: 5, 520: 7, 522: 4, 524: 4, 736: 8, 738: 8, 740: 8, 742: 8, 744: 8, 746: 5, 748: 8, 750: 3, 751: 1, 752: 8, 754: 8, 756: 5, 758: 1, 760: 5, 762: 3, 875: 8, 994: 4, 996: 6, 998: 5, 1002: 8, 1004: 8, 1006: 7, 1228: 8, 1232: 8, 1236: 8, 1238: 4, 1240: 8, 1242: 8, 1244: 8, 1246: 8, 1248: 8, 1250: 8, 1252: 8, 1254: 2, 1256: 2, 1258: 8, 1260: 8, 1262: 8, 1264: 7, 1266: 5, 1268: 8, 1375: 8, 1492: 4, 1494: 4, 1496: 6, 1498: 2, 1500: 4, 1502: 8, 1504: 7, 1508: 8, 1510: 8, 1625: 4, 1627: 1, 1746: 1, 1752: 2, 1754: 4, 1756: 4, 1992: 3, 1994: 2, 1996: 2, 1999: 5, 2000: 8, 2002: 2, 2004: 8, 2006: 3, 2008: 4, 2015: 8, 2016: 8},
    {242: 7, 244: 7, 247: 8, 253: 6, 254: 4, 480: 8, 482: 8, 484: 8, 486: 8, 488: 5, 490: 4, 492: 8, 494: 6, 496: 8, 498: 8, 500: 7, 502: 4, 504: 8, 505: 8, 507: 8, 508: 8, 510: 5, 512: 8, 514: 8, 520: 7, 521: 8, 522: 4, 524: 4, 688: 8, 690: 8, 692: 8, 736: 8, 738: 8, 740: 8, 742: 8, 744: 8, 746: 5, 747: 8, 748: 8, 750: 3, 751: 8, 752: 8, 754: 8, 756: 8, 758: 1, 760: 5, 762: 3, 875: 8, 994: 4, 996: 6, 997: 6, 998: 5, 1002: 8, 1004: 8, 1006: 8, 1228: 8, 1230: 8, 1232: 8, 1234: 1, 1236: 8, 1238: 4, 1240: 8, 1242: 8, 1244: 8, 1246: 8, 1248: 8, 1250: 8, 1252: 8, 1254: 2, 1256: 2, 1258: 8, 1259: 8, 1260: 8, 1262: 8, 1264: 7, 1268: 8, 1375: 8, 1492: 4, 1494: 4, 1496: 6, 1498: 2, 1500: 4, 1502: 8, 1504: 7, 1505: 8, 1508: 8, 1510: 8, 1625: 4, 1626: 8, 1627: 1, 1628: 8, 1629: 8, 1746: 1, 1752: 2, 1754: 4, 1756: 4, 1992: 8, 1993: 8, 1994: 2, 1996: 2, 1999: 5, 2000: 8, 2002: 2, 2004: 8, 2006: 3, 2008: 4},
  ],
}

DBC = {
  CAR.JEEP_CHEROKEE_SRT_2014: dbc_dict(
    'jeep_cherokee_srt_2014', # 'pt'
    'lrr3_chrysler_200_kl_private_fusion'),  # 'radar'
  CAR.CHRYSLER_200_V6: dbc_dict(
    'lrr3_chrysler_200_kl', # 'pt'
    'lrr3_chrysler_200_kl_private_fusion'),  # 'radar'
  CAR.KL_CHEROKEE: dbc_dict(
    'lrr3_chrysler_200_kl', # 'pt'
    'lrr3_chrysler_200_kl_private_fusion'),  # 'radar'
}

STEER_THRESHOLD = 120


ECU_FINGERPRINT = {
  Ecu.fwdCamera: [0x1f6],   # lkas cmd
}
