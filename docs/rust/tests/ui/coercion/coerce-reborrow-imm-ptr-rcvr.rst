tests/ui/coercion/coerce-reborrow-imm-ptr-rcvr.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct SpeechMaker {
    speeches: usize
}

impl SpeechMaker {
    pub fn how_many(&self) -> usize { self.speeches }
}

fn foo(speaker: &SpeechMaker) -> usize {
    speaker.how_many() + 33
}

pub fn main() {
    let lincoln = SpeechMaker {speeches: 22};
    assert_eq!(foo(&lincoln), 55);
}


