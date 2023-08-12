src/main.rs
===========

Last edited: 2022-09-09 01:48:54

Contents:

.. code-block:: rs

    use anyhow::Result;
use console::{style, Emoji, Style};
use dialoguer::{theme::ColorfulTheme, Input};
use retry::{delay::Exponential, retry};
use std::{
    env,
    fs::{self, OpenOptions},
    io::Write,
    path::Path,
    ptr,
    time::Duration,
};
use winapi::{
    shared::minwindef::*,
    um::winuser::{SendMessageTimeoutA, HWND_BROADCAST, SMTO_ABORTIFHUNG, WM_SETTINGCHANGE},
};
use winreg::{enums::HKEY_CURRENT_USER, RegKey};

const DOWNLOAD_PATH: &str =
    "https://github.com/metaplex-foundation/sugar/releases/latest/download/sugar-windows-latest.exe";

const COMPLETE_EMOJI: Emoji<'_, '_> = Emoji("✅ ", "");
const ERROR_EMOJI: Emoji<'_, '_> = Emoji("🛑 ", "");

fn main() {
    match run() {
        Ok(()) => {
            println!(
                "\n{}{}",
                COMPLETE_EMOJI,
                style("Sugar successfully installed!").green().bold().dim()
            );

            // Give user time to read messages.
            std::thread::sleep(Duration::from_secs(3));
        }
        Err(err) => {
            println!(
                "\n{}{} {}",
                ERROR_EMOJI,
                style("Error installing Sugar):").red(),
                err,
            );
            let _: String = Input::with_theme(&get_theme())
                .with_prompt("Exit?")
                .interact()
                .unwrap();
            // finished the program with an error code to the OS
            std::process::exit(1);
        }
    }
}

fn run() -> Result<()> {
    if !cfg!(windows) {
        println!("For Linux and MacOS systems use the install script in the Sugar README.");
        std::process::exit(1);
    }

    let drive = env::var_os("HOMEDRIVE").expect("Couldn't find Windows home drive key.");
    let path = env::var_os("HOMEPATH").expect("Couldn't find Windows home path key.");
    let local_app_data = env::var_os("LOCALAPPDATA").expect("Couldn't find LOCALAPPDATA path key.");

    let home = Path::new(&drive).join(&path).as_os_str().to_owned();
    let cargo_bin_path = Path::new(&home).join(".cargo").join("bin");
    let local_app_data_path = Path::new(&local_app_data).join("SugarCLI");

    // Prefer to install to .cargo/bin if it exists, otherwise use LOCALAPPDATA.
    if cargo_bin_path.exists() {
        println!("Installing to .cargo/bin...");
        let mut f = OpenOptions::new()
            .read(true)
            .write(true)
            .create(true)
            .open(&cargo_bin_path.join("sugar.exe"))?;

        fetch_binary(&mut f)?;
    } else {
        println!("Installing to LocalAppData...");

        // Create SugarCLI folder in LOCALAPPDATA if it doesn't already exist.
        if !local_app_data_path.exists() {
            fs::create_dir(&local_app_data_path)?;
        }

        let mut f = OpenOptions::new()
            .read(true)
            .write(true)
            .create(true)
            .open(&local_app_data_path.join("sugar.exe"))?;

        // Add to PATH if not already present.
        let hkcu = RegKey::predef(HKEY_CURRENT_USER);
        let (env, _) = hkcu.create_subkey("Environment")?;
        let mut path: String = env.get_value("path")?;
        if !path.contains(local_app_data_path.to_str().unwrap()) {
            path.push(';');
            path.push_str(local_app_data_path.to_str().unwrap());
            env.set_value("path", &path)?;
        }

        fetch_binary(&mut f)?;
    }

    // Signal other processes to update their environments so the new path is registered.
    println!("Refreshing PATH...");
    unsafe {
        SendMessageTimeoutA(
            HWND_BROADCAST,
            WM_SETTINGCHANGE,
            0 as WPARAM,
            "Environment\0".as_ptr() as LPARAM,
            SMTO_ABORTIFHUNG,
            5000,
            ptr::null_mut(),
        );
    }

    Ok(())
}

fn fetch_binary<F: Write>(f: &mut F) -> Result<()> {
    println!("Getting binary....");
    let contents = retry(
        Exponential::from_millis_with_factor(100, 2.0).take(5),
        || reqwest::blocking::get(DOWNLOAD_PATH)?.bytes(),
    )?;
    println!("Writing binary....");
    f.write_all(&contents)?;

    Ok(())
}

fn get_theme() -> ColorfulTheme {
    ColorfulTheme {
        prompt_style: Style::new(),
        checked_item_prefix: style("✔".to_string()).green().force_styling(true),
        unchecked_item_prefix: style("✔".to_string()).black().force_styling(true),
        ..Default::default()
    }
}


