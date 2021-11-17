from enum import IntFlag


class DeviceMode(IntFlag):
    ReadOnly = 0x1
    WriteOnly = 0x2
    ReadWrite = ReadOnly | WriteOnly