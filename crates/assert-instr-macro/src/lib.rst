crates/assert-instr-macro/src/lib.rs
====================================

Last edited: 2019-05-15 21:04:28

Contents:

.. code-block:: rs

    //! Implementation of the `#[assert_instr]` macro
//!
//! This macro is used when testing the `stdsimd` crate and is used to generate
//! test cases to assert that functions do indeed contain the instructions that
//! we're expecting them to contain.
//!
//! The procedural macro here is relatively simple, it simply appends a
//! `#[test]` function to the original token stream which asserts that the
//! function itself contains the relevant instruction.

extern crate proc_macro;
extern crate proc_macro2;
#[macro_use]
extern crate quote;
extern crate syn;

use proc_macro2::TokenStream;
use quote::ToTokens;

#[proc_macro_attribute]
pub fn assert_instr(
    attr: proc_macro::TokenStream,
    item: proc_macro::TokenStream,
) -> proc_macro::TokenStream {
    let invoc = match syn::parse::<Invoc>(attr) {
        Ok(s) => s,
        Err(e) => return e.to_compile_error().into(),
    };
    let item = match syn::parse::<syn::Item>(item) {
        Ok(s) => s,
        Err(e) => return e.to_compile_error().into(),
    };
    let func = match item {
        syn::Item::Fn(ref f) => f,
        _ => panic!("must be attached to a function"),
    };

    let instr = &invoc.instr;
    let name = &func.ident;

    // Disable assert_instr for x86 targets compiled with avx enabled, which
    // causes LLVM to generate different intrinsics that the ones we are
    // testing for.
    let disable_assert_instr = std::env::var("STDSIMD_DISABLE_ASSERT_INSTR").is_ok();

    let instr_str = instr
        .replace('.', "_")
        .replace('/', "_")
        .replace(':', "_")
        .replace(char::is_whitespace, "");
    let assert_name = syn::Ident::new(&format!("assert_{}_{}", name, instr_str), name.span());
    let shim_name = syn::Ident::new(&format!("{}_shim_{}", name, instr_str), name.span());
    let mut inputs = Vec::new();
    let mut input_vals = Vec::new();
    let ret = &func.decl.output;
    for arg in func.decl.inputs.iter() {
        let capture = match *arg {
            syn::FnArg::Captured(ref c) => c,
            ref v => panic!(
                "arguments must not have patterns: `{:?}`",
                v.clone().into_token_stream()
            ),
        };
        let ident = match capture.pat {
            syn::Pat::Ident(ref i) => &i.ident,
            _ => panic!("must have bare arguments"),
        };
        if let Some(&(_, ref tts)) = invoc.args.iter().find(|a| *ident == a.0) {
            input_vals.push(quote! { #tts });
        } else {
            inputs.push(capture);
            input_vals.push(quote! { #ident });
        }
    }

    let attrs = func
        .attrs
        .iter()
        .filter(|attr| {
            attr.path
                .segments
                .first()
                .expect("attr.path.segments.first() failed")
                .value()
                .ident
                .to_string()
                .starts_with("target")
        })
        .collect::<Vec<_>>();
    let attrs = Append(&attrs);

    // Use an ABI on Windows that passes SIMD values in registers, like what
    // happens on Unix (I think?) by default.
    let abi = if cfg!(windows) {
        syn::LitStr::new("vectorcall", proc_macro2::Span::call_site())
    } else {
        syn::LitStr::new("C", proc_macro2::Span::call_site())
    };
    let shim_name_str = format!("{}{}", shim_name, assert_name);
    let to_test = quote! {
        #attrs
        #[no_mangle]
        unsafe extern #abi fn #shim_name(#(#inputs),*) #ret {
            // The compiler in optimized mode by default runs a pass called
            // "mergefunc" where it'll merge functions that look identical.
            // Turns out some intrinsics produce identical code and they're
            // folded together, meaning that one just jumps to another. This
            // messes up our inspection of the disassembly of this function and
            // we're not a huge fan of that.
            //
            // To thwart this pass and prevent functions from being merged we
            // generate some code that's hopefully very tight in terms of
            // codegen but is otherwise unique to prevent code from being
            // folded.
            ::stdsimd_test::_DONT_DEDUP = #shim_name_str;
            #name(#(#input_vals),*)
        }
    };

    // If instruction tests are disabled avoid emitting this shim at all, just
    // return the original item without our attribute.
    if !cfg!(optimized) || disable_assert_instr {
        return (quote! { #item }).into();
    }

    let tts: TokenStream = quote! {
        #[cfg_attr(target_arch = "wasm32", wasm_bindgen_test)]
        #[cfg_attr(not(target_arch = "wasm32"), test)]
        #[allow(non_snake_case)]
        fn #assert_name() {
            #to_test

            ::stdsimd_test::assert(#shim_name as usize,
                                   stringify!(#shim_name),
                                   #instr);
        }
    };
    // why? necessary now to get tests to work?
    let tts: TokenStream = tts.to_string().parse().expect("cannot parse tokenstream");

    let tts: TokenStream = quote! {
        #item
        #tts
    };
    tts.into()
}

struct Invoc {
    instr: String,
    args: Vec<(syn::Ident, syn::Expr)>,
}

impl syn::parse::Parse for Invoc {
    fn parse(input: syn::parse::ParseStream) -> syn::parse::Result<Self> {
        use syn::{ext::IdentExt, Token};

        let mut instr = String::new();
        while !input.is_empty() {
            if input.parse::<Token![,]>().is_ok() {
                break;
            }
            if let Ok(ident) = syn::Ident::parse_any(input) {
                instr.push_str(&ident.to_string());
                continue;
            }
            if input.parse::<Token![.]>().is_ok() {
                instr.push_str(".");
                continue;
            }
            if let Ok(s) = input.parse::<syn::LitStr>() {
                instr.push_str(&s.value());
                continue;
            }
            println!("{:?}", input.cursor().token_stream());
            return Err(input.error("expected an instruction"));
        }
        if instr.is_empty() {
            return Err(input.error("expected an instruction before comma"));
        }
        let mut args = Vec::new();
        while !input.is_empty() {
            let name = input.parse::<syn::Ident>()?;
            input.parse::<Token![=]>()?;
            let expr = input.parse::<syn::Expr>()?;
            args.push((name, expr));

            if input.parse::<Token![,]>().is_err() {
                if !input.is_empty() {
                    return Err(input.error("extra tokens at end"));
                }
                break;
            }
        }
        Ok(Self { instr, args })
    }
}

struct Append<T>(T);

impl<T> quote::ToTokens for Append<T>
where
    T: Clone + IntoIterator,
    T::Item: quote::ToTokens,
{
    fn to_tokens(&self, tokens: &mut proc_macro2::TokenStream) {
        for item in self.0.clone() {
            item.to_tokens(tokens);
        }
    }
}


