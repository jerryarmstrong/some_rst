lldb/examples/summaries/synth.py
================================

Last edited: 2023-03-17 20:18:30

Contents:

.. code-block:: py

    import lldb


class PythonObjectSyntheticChildProvider(object):

    def __init__(self, value, internal_dict):
        self.value = value
        self.values = self.make_children()
        self.built_values = {}
        self.bo = self.value.target.byte_order
        self.ps = self.value.target.addr_size

    def make_children(self):
        pass

    def num_children(self):
        return len(self.values)

    def get_child_index(self, name):
        i = 0
        for N, value in self.values:
            if N == name:
                return i
            i += 1
        return None

    def update(self):
        pass

    def has_children(self):
        return len(self.values) > 0

    def gen_child(self, name, value):
        data = None
        type = None
        import six
        if isinstance(value, six.integer_types):
            data = lldb.SBData.CreateDataFromUInt64Array(
                self.bo, self.ps, [value])
            type = self.value.target.GetBasicType(lldb.eBasicTypeLong)
        elif isinstance(value, float):
            data = lldb.SBData.CreateDataFromDoubleArray(
                self.bo, self.ps, [value])
            type = self.value.target.GetBasicType(lldb.eBasicTypeDouble)
        elif isinstance(value, str):
            data = lldb.SBData.CreateDataFromCString(self.bo, self.ps, value)
            type = self.value.target.GetBasicType(
                lldb.eBasicTypeChar).GetArrayType(
                len(value))
        if (data is not None) and (type is not None):
            return self.value.CreateValueFromData(name, data, type)
        return None

    def get_child_at_index(self, index):
        if index in self.built_values:
            return self.built_values[index]

        bv = None

        name, value = self.values[index]
        bv = self.gen_child(name, value)
        self.built_values[index] = bv
        return bv


