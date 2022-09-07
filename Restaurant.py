print('Welcome to Nigerian Restaurants Searcher =)')


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.choices = []
    def add_child(self, node):
        self.choices.append(node)
    def traverse(self):
        main_node = self
        print(main_node.value)
        while len(main_node.choices) > 0:
            choice = input("Enter: ")
            if choice is None:
                print("You're not ready to eat")
            if choice is not None:
                choicer = choice.lower()
                indexer = sum(choicer.encode())
                index = indexer % 3
                if index == 0:
                    print('Lovely')
                    main = main_node.choices[index]
                    print(main.value)
                    main_node = main
                if index == 1:
                    print('Amazing')
                    main = main_node.choices[index]
                    print(main.value)
                    main_node = main
                if index == 2:
                    print('Spectacular')
                    main = main_node.choices[index]
                    print(main.value)
                    main_node = main


                





Restaurant = TreeNode("Choose you location: Lagos, Imo or Abuja")
Lagos = TreeNode("Choose your delicacy: Ewa Agonyin, Fried Rice, Jollof Rice:")
Imo = TreeNode("Choose your delicacy: Spaghetti, Miyan Kaka, Danwake:")
Abuja = TreeNode("Choose your delicacy: Roast Goat Meat, Semo with White Soup, Ofe Owerri:")
One = TreeNode("Food is being prepared. Select a drink from Fanta, Fruit Juice and Lukewarm Water")
Two = TreeNode("Food is being prepared. Select a drink from Fanta, Fruit Juice and Lukewarm Water")
Three = TreeNode("Food is being prepared. Select a drink from Fanta, Fruit Juice and Lukewarm Water")
Fanta = TreeNode("Fantastic. Please Wait")
Juice = TreeNode("Juicy Choice. Please Wait")
Water = TreeNode("Wonderful. Please Wait")
Restaurant.add_child(Lagos)
Restaurant.add_child(Imo)
Restaurant.add_child(Abuja)
Lagos.add_child(One)
Lagos.add_child(Two)
Lagos.add_child(Three)
Imo.add_child(One)
Imo.add_child(Two)
Imo.add_child(Three)
Abuja.add_child(One)
Abuja.add_child(Two)
Abuja.add_child(Three)
One.add_child(Fanta)
One.add_child(Juice)
One.add_child(Water)
Two.add_child(Fanta)
Two.add_child(Juice)
Two.add_child(Water)
Three.add_child(Fanta)
Three.add_child(Juice)
Three.add_child(Water)











Restaurant.traverse()
