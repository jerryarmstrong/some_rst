library/core/tests/asserting.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use core::asserting::{Capture, TryCaptureGeneric, TryCapturePrintable, Wrapper};

macro_rules! test {
    ($test_name:ident, $elem:expr, $captured_elem:expr, $output:literal) => {
        #[test]
        fn $test_name() {
            let elem = $elem;
            let mut capture = Capture::new();
            assert!(capture.elem == None);
            (&Wrapper(&elem)).try_capture(&mut capture);
            assert!(capture.elem == $captured_elem);
            assert_eq!(format!("{:?}", capture), $output);
        }
    };
}

#[derive(Debug, PartialEq)]
struct NoCopy;

#[derive(PartialEq)]
struct NoCopyNoDebug;

#[derive(Clone, Copy, PartialEq)]
struct NoDebug;

test!(
    capture_with_non_copyable_and_non_debugabble_elem_has_correct_params,
    NoCopyNoDebug,
    None,
    "N/A"
);

test!(capture_with_non_copyable_elem_has_correct_params, NoCopy, None, "N/A");

test!(capture_with_non_debugabble_elem_has_correct_params, NoDebug, None, "N/A");

test!(capture_with_copyable_and_debugabble_elem_has_correct_params, 1i32, Some(1i32), "1");


