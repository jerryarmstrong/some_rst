src/tools/rustfmt/tests/source/issue-855.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    'running: loop {
        for event in event_pump.poll_iter() {
            match event {
                Event::Quit {..} | Event::KeyDown { keycode: Some(Keycode::Escape), .. } => break 'running,
            }
        }
    }
}

fn main2() {
    'running: loop {
        for event in event_pump.poll_iter() {
            match event {
                Event::Quit {..} |
                Event::KeyDownXXXXXXXXXXXXX { keycode: Some(Keycode::Escape), .. } => break 'running,
            }
        }
    }
}


