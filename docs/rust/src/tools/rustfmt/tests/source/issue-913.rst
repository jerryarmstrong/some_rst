src/tools/rustfmt/tests/source/issue-913.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod client {
    impl Client {
        fn test(self) -> Result<()> {
            let next_state = match self.state {
                State::V5(v5::State::Command(v5::coand::State::WriteVersion(ref mut response))) => {
                         let x   =   reformat . meeee()  ; 
                }
            };

            let next_state = match self.state {
                State::V5(v5::State::Command(v5::comand::State::WriteVersion(ref mut response))) => {
                    // The pattern cannot be formatted in a way that the match stays
                    // within the column limit. The rewrite should therefore be
                    // skipped.
                    let x =  dont . reformat . meeee();
                }
            };
        }
    }
}


