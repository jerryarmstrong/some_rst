src/tools/rustfmt/tests/target/issue-1397.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub enum TransactionState {
    Committed(i64),
}

pub enum Packet {
    Transaction { state: TransactionState },
}

fn baz(p: Packet) {
    loop {
        loop {
            loop {
                loop {
                    if let Packet::Transaction {
                        state: TransactionState::Committed(ts, ..),
                        ..
                    } = p
                    {
                        unreachable!()
                    }
                }
            }
        }
    }
}


