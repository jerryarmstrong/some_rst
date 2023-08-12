src/v2/utils/asTime.js
======================

Last edited: 2020-03-22 10:28:18

Contents:

.. code-block:: js

    import formatDistanceToNow from 'date-fns/formatDistanceToNow';
import isValid from 'date-fns/isValid';
import parseISO from 'date-fns/parseISO';

function asTime(value) {
  const parsed = parseISO(value);
  if (!value || !isValid(parsed)) return '';
  return formatDistanceToNow(parsed, {addSuffix: true});
}

export default asTime;


