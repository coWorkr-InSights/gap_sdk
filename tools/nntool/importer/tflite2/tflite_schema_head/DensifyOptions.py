# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_schema_head

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class DensifyOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsDensifyOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DensifyOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def DensifyOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # DensifyOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

def DensifyOptionsStart(builder): builder.StartObject(0)
def DensifyOptionsEnd(builder): return builder.EndObject()
