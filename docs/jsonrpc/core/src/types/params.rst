core/src/types/params.rs
========================

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    //! jsonrpc params field

use serde::de::{DeserializeOwned};
use serde_json;
use serde_json::value::from_value;

use super::{Value, Error};

/// Request parameters
#[derive(Debug, PartialEq, Clone, Serialize, Deserialize)]
#[serde(untagged)]
pub enum Params {
	/// No parameters
	None,
	/// Array of values
	Array(Vec<Value>),
	/// Map of values
	Map(serde_json::Map<String, Value>),
}

impl Params {
	/// Parse incoming `Params` into expected types.
	pub fn parse<D>(self) -> Result<D, Error> where D: DeserializeOwned {
		let value = match self {
			Params::Array(vec) => Value::Array(vec),
			Params::Map(map) => Value::Object(map),
			Params::None =>  Value::Null
		};

		from_value(value).map_err(|e| {
			Error::invalid_params(format!("Invalid params: {}.", e))
		})
	}
}

#[cfg(test)]
mod tests {
	use serde_json;
	use super::Params;
	use types::{Value, Error, ErrorCode};

	#[test]
	fn params_deserialization() {
		let s = r#"[null, true, -1, 4, 2.3, "hello", [0], {"key": "value"}, []]"#;
		let deserialized: Params = serde_json::from_str(s).unwrap();

		let mut map = serde_json::Map::new();
		map.insert("key".to_string(), Value::String("value".to_string()));

		assert_eq!(Params::Array(vec![
								 Value::Null, Value::Bool(true), Value::from(-1), Value::from(4),
								 Value::from(2.3), Value::String("hello".to_string()),
								 Value::Array(vec![Value::from(0)]), Value::Object(map),
								 Value::Array(vec![]),
		]), deserialized);
	}

	#[test]
	fn should_return_meaningful_error_when_deserialization_fails() {
		// given
		let s = r#"[1, true]"#;
		let params = || serde_json::from_str::<Params>(s).unwrap();

		// when
		let v1: Result<(Option<u8>, String), Error> = params().parse();
		let v2: Result<(u8, bool, String), Error> = params().parse();
		let err1 = v1.unwrap_err();
		let err2 = v2.unwrap_err();

		// then
		assert_eq!(err1.code, ErrorCode::InvalidParams);
		assert_eq!(err1.message, "Invalid params: invalid type: boolean `true`, expected a string.");
		assert_eq!(err1.data, None);
		assert_eq!(err2.code, ErrorCode::InvalidParams);
		assert_eq!(err2.message, "Invalid params: invalid length 2, expected a tuple of size 3.");
		assert_eq!(err2.data, None);
	}
}


