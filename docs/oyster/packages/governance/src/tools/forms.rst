packages/governance/src/tools/forms.ts
======================================

Last edited: 2023-07-19 16:40:40

Contents:

.. code-block:: ts

    export const formVerticalLayout = {
  labelCol: { span: 24 },
  wrapperCol: { span: 24 },
};

/* eslint-disable no-template-curly-in-string */
export const formValidateMessages = {
  required: 'Please provide ${label}',
};
/* eslint-enable no-template-curly-in-string */

export const formDefaults = {
  requiredMark: false,
  ...formVerticalLayout,
  validateMessages: formValidateMessages,
};


