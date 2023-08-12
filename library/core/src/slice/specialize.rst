library/core/src/slice/specialize.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub(super) trait SpecFill<T> {
    fn spec_fill(&mut self, value: T);
}

impl<T: Clone> SpecFill<T> for [T] {
    default fn spec_fill(&mut self, value: T) {
        if let Some((last, elems)) = self.split_last_mut() {
            for el in elems {
                el.clone_from(&value);
            }

            *last = value
        }
    }
}

impl<T: Copy> SpecFill<T> for [T] {
    fn spec_fill(&mut self, value: T) {
        for item in self.iter_mut() {
            *item = value;
        }
    }
}


