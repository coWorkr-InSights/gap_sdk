# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_schema_head

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SpaceToDepthOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsSpaceToDepthOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SpaceToDepthOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def SpaceToDepthOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # SpaceToDepthOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SpaceToDepthOptions
    def BlockSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def SpaceToDepthOptionsStart(builder): builder.StartObject(1)
def SpaceToDepthOptionsAddBlockSize(builder, blockSize): builder.PrependInt32Slot(0, blockSize, 0)
def SpaceToDepthOptionsEnd(builder): return builder.EndObject()
