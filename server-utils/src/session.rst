server-utils/src/session.rs
===========================

Last edited: 2018-12-07 22:58:36

Contents:

.. code-block:: rs

    //! Session statistics.

/// Session id
pub type SessionId = u64;

/// Keeps track of open sessions
pub trait SessionStats: Send + Sync + 'static {
	/// Executed when new session is opened.
	fn open_session(&self, id: SessionId);
	/// Executed when session is closed.
	fn close_session(&self, id: SessionId);
}


