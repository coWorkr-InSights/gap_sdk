# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_schema_head

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SplitOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSplitOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SplitOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def SplitOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # SplitOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SplitOptions
    def NumSplits(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def SplitOptionsStart(builder): builder.StartObject(1)
def SplitOptionsAddNumSplits(builder, numSplits): builder.PrependInt32Slot(0, numSplits, 0)
def SplitOptionsEnd(builder): return builder.EndObject()
