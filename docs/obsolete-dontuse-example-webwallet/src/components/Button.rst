src/components/Button.js
========================

Last edited: 2020-08-30 15:21:22

Contents:

.. code-block:: js

    import React from 'react';
import PropTypes from 'prop-types';

const Button = props => {
  return (
    <div className={`app-btn ${props.disabled && 'disabled'}`}>
      <button {...props} />
    </div>
  );
};

Button.propTypes = {
  disabled: PropTypes.bool,
};

export default Button;


