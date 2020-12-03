# automatically generated by the FlatBuffers compiler, do not modify

# namespace: tflite_schema_head

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ResizeNearestNeighborOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsResizeNearestNeighborOptions(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ResizeNearestNeighborOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def ResizeNearestNeighborOptionsBufferHasIdentifier(cls, buf, offset, size_prefixed=False):
        return flatbuffers.util.BufferHasIdentifier(buf, offset, b"\x54\x46\x4C\x33", size_prefixed=size_prefixed)

    # ResizeNearestNeighborOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ResizeNearestNeighborOptions
    def AlignCorners(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # ResizeNearestNeighborOptions
    def HalfPixelCenters(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def ResizeNearestNeighborOptionsStart(builder): builder.StartObject(2)
def ResizeNearestNeighborOptionsAddAlignCorners(builder, alignCorners): builder.PrependBoolSlot(0, alignCorners, 0)
def ResizeNearestNeighborOptionsAddHalfPixelCenters(builder, halfPixelCenters): builder.PrependBoolSlot(1, halfPixelCenters, 0)
def ResizeNearestNeighborOptionsEnd(builder): return builder.EndObject()
