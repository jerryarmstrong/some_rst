example/src/App.tsx
===================

Last edited: 2023-03-27 15:10:41

Contents:

.. code-block:: tsx

    import * as React from 'react';

import { StyleSheet, View, Text } from 'react-native';
import { multiply } from 'mobile-wallet-adapter';

export default function App() {
  const [result, setResult] = React.useState<number | undefined>();

  React.useEffect(() => {
    multiply(3, 7).then(setResult);
  }, []);

  return (
    <View style={styles.container}>
      <Text>Result: {result}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  box: {
    width: 60,
    height: 60,
    marginVertical: 20,
  },
});


