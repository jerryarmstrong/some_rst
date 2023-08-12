packages/app-mobile/src/navigation/TokenPriceNavigator.tsx
==========================================================

Last edited: 2023-07-01 03:20:04

Contents:

.. code-block:: tsx

    import { createStackNavigator } from "@react-navigation/stack";

import { HeaderButton } from "~navigation/components";
import { TokenPriceStackParamList } from "~navigation/types";
import { TokenPriceDetailScreen } from "~screens/TokenPriceDetailScreen";
import { TokenPriceListScreen } from "~screens/TokenPriceListScreen";

const Stack = createStackNavigator<TokenPriceStackParamList>();
export function TokenPriceNavigator(): JSX.Element {
  // const theme = useTheme();
  return (
    <Stack.Navigator
    // screenOptions={
    //   {
    //     headerTintColor: theme.custom.colors.fontColor,
    //     headerBackTitleVisible: false,
    //   }
    // }
    >
      <Stack.Screen
        name="TokenPriceList"
        component={TokenPriceListScreen}
        options={{ title: "Token Prices" }}
      />
      <Stack.Screen
        name="TokenPriceDetail"
        component={TokenPriceDetailScreen}
        options={({ route }) => {
          return {
            title: route.params.title,
            headerRight: () => <HeaderButton name="star-outline" />,
          };
        }}
      />
    </Stack.Navigator>
  );
}


