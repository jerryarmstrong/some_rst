src/components/Screen.tsx
=========================

Last edited: 2023-07-18 02:03:22

Contents:

.. code-block:: tsx

    import { View, StyleSheet, StyleProp, ViewStyle } from "react-native";

type Props = {
  style?: StyleProp<ViewStyle>;
  children: JSX.Element | JSX.Element[] | null;
};
export function Screen({ style, children }: Props) {
  return <View style={[styles.screen, style]}>{children}</View>;
}

const styles = StyleSheet.create({
  screen: {
    flex: 1,
    padding: 12,
  },
});


