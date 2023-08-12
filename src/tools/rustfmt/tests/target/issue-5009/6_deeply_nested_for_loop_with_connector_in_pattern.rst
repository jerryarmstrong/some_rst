src/tools/rustfmt/tests/target/issue-5009/6_deeply_nested_for_loop_with_connector_in_pattern.rs
===============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    for variable_in_a /* ... */ in 0..1 {
        for variable_in_b /* ... */ in 0..1 {
            for variable_in_c /* ... */ in 0..1 {
                for variable_in_d /* ... */ in 0..1 {
                    for variable_in_e /* ... */ in 0..1 {
                        for variable_in_f /* ... */ in 0..1 {
                            for variable_in_g /* ... */ in 0..1 {
                                for variable_in_h /* ... */ in 0..1 {
                                    for variable_in_i /* ... */ in 0..1 {
                                        for variable_in_j /* ... */ in 0..1 {
                                            for variable_in_k /* ... */ in 0..1 {
                                                for variable_in_l /* ... */ in 0..1 {
                                                    for variable_in_m /* ... */ in 0..1 {
                                                        for variable_in_n /* ... */ in 0..1 {
                                                            for variable_in_o /* ... */ in 0..1 {
                                                            }
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}


