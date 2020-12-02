# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_schema_head

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class DivOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsDivOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = DivOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def DivOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # DivOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # DivOptions
    def FusedActivationFunction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

def DivOptionsStart(builder): builder.StartObject(1)
def DivOptionsAddFusedActivationFunction(builder, fusedActivationFunction): builder.PrependInt8Slot(0, fusedActivationFunction, 0)
def DivOptionsEnd(builder): return builder.EndObject()
