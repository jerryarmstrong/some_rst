src/tools/clippy/tests/ui-toml/upper_case_acronyms_aggressive/upper_case_acronyms.rs
====================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::upper_case_acronyms)]

struct HTTPResponse; // not linted by default, but with cfg option

struct CString; // not linted

enum Flags {
    NS, // not linted
    CWR,
    ECE,
    URG,
    ACK,
    PSH,
    RST,
    SYN,
    FIN,
}

// linted with cfg option, beware that lint suggests `GccllvmSomething` instead of
// `GccLlvmSomething`
struct GCCLLVMSomething;

// don't warn on public items
pub struct MIXEDCapital;

pub struct FULLCAPITAL;

// enum variants should not be linted if the num is pub
pub enum ParseError<T> {
    FULLCAPITAL(u8),
    MIXEDCapital(String),
    Utf8(std::string::FromUtf8Error),
    Parse(T, String),
}

// private, do lint here
enum ParseErrorPrivate<T> {
    WASD(u8),
    WASDMixed(String),
    Utf8(std::string::FromUtf8Error),
    Parse(T, String),
}

fn main() {}


