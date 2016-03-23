import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT_project.settings')

import django
django.setup()

from ChineseFoodRank.models import Category, Food, Style


def populate():
    sour_style = add_style('Sour')
    sweet_style = add_style("Sweet")
    salty_style = add_style("Salty")
    hot_style = add_style("Hot")

    starters_cat = add_cat("starters")
    sidedishes_cat = add_cat("sidedishes")
    vegetables_cat = add_cat("vegetables")
    pork_cat = add_cat("pork")
    beef_cat = add_cat("beef")
    chicken_cat = add_cat("chicken")
    duck_cat=add_cat("duck")
    fish_cat=add_cat("fish")
    other_cat=add_cat("other")


    add_food(
        foodid=1,
        style=sour_style,
        cat = pork_cat,
        likes = 40,
        description="This sweet and sour pork is prepared American-sytle with more batter and deep-fried twice for extra crispiness",
        title="Sweet and Sour Pork",
        url="http://127.0.0.1:8000/media/food_images/1.jpg")

    add_food(
        foodid=2,
        style=sweet_style,
        cat = pork_cat,
        likes = 18,
        description="Slow cooking beef shin or brisket in Asian aromatic spices gives a melt-in-the-mouth main course that's delicious with steamed rice and crisp stir-fried vegetables",
        title="braised beef with brown sauce",
        url="http://127.0.0.1:8000/media/food_images/2.jpg")

    add_food(
        foodid=3,
        style=salty_style,
        cat = pork_cat,
        likes =14,
        description="Louver knot pork is the Han dishes in Jiangnan area. Louver knot is also called tofu skin, thin as paper, rib like pimp, and cheap. Bean curd skin rich nutritional value. In the south the louver knot called bean curd skin or Yuba; in the North was called hundreds of leaf node.",
        title="Stewed Pork Cubes and Tufu Skin in Brown Sauce",
        url="http://127.0.0.1:8000/media/food_images/3.jpg")

    add_food(
        foodid=5,
        style=sour_style,
        cat = beef_cat,
        likes = 22,
        description="Braised with lots of browned onions, carrots, and celery in a mix of chicken broth and crushed tomatoes, the beef exits the oven full-flavored and fork-tender, ready to be shredded for the country hash or sliced and served with mashed potatoes for a homey dinner (though it's even better if you can wait a day). By all means, freeze the leftover braising liquid; it's wonderful as a sauce for fettuccine or as the base for a vegetable barley soup.",
        title="Braised Beef Brisket with Tomato",
        url="http://127.0.0.1:8000/media/food_images/4.jpg")

    add_food(
        foodid=4,
        style=salty_style,
        cat = beef_cat,
        likes = 28,
        description="Black pepper beef looks dark in color and tastes strong. The beef in it tastes smooth and tender after frying in the oil; the onion in the dish is fragrant and crispy, while the green pepper makes it more fresh and eye-catching.One of the local characteristic dishes of Guangdong Cuisine, black pepper beef is a good choice for people who like spicy food. Black pepper is a spicy and hot seasoning, which can help people to withstand the cold and the dampness. Besides beef, Chinese people also cook black pepper chicken and black pepper pork.",
        title="Sauteed Beef Filet with Black Pepper",
        url="http://127.0.0.1:8000/media/food_images/5.jpg")

    add_food(
        foodid=6,
        style=hot_style,
        cat = beef_cat,
        likes = 33,
        description="It is rich in taste and bright in color, highlighting the unique spicy and hot flavor of Sichuan Cuisine. The beef in it tastes fresh, tender and smooth, while the green vegetables palatable and fresh.Representative of the poached dishes in Sichuan Cuisine, this dish is warmly welcomed among the Chinese. The beef in it is cooked in the chili soup instead of being stir-fried by oil until done, hence its name. The main ingredients are beef and some vegetables such as bean sprout, celery, green vegetables, and lettuce. It is a very nutritious dish, combining the rich protein in beef, the multi-vitamins in bean sprouts and various nutritious elements in green vegetables.",
        title="Poached Sliced Beef in Hot Chili Oil",
        url="http://127.0.0.1:8000/media/food_images/6.jpg")

    add_food(
        foodid=7,
        style=salty_style,
        cat = other_cat,
        likes = 36,
        description="Boiled lamb is what Mongolians call -red food, or meat that is meant to be eaten with the hands. For herdsmen, boiled lamb is a plain, traditional meal, one that has endured for a thousand years.To make it, the mutton is removed from the bone and put into a pot of boiling water, without sauce or salt. To eat it, you grasp the bone with one hand and cut the meat with the other, then dip the mutton into whatever seasoning is offered. Herdsmen usually have this dish for dinner.",
        title="Mongolian Boiled Lamb",
        url="http://127.0.0.1:8000/media/food_images/7.jpg")

    add_food(
        foodid=8,
        style=hot_style,
        cat = other_cat,
        likes = 12,
        description="Braised mutton was originally a Hui cuisine, with a long history. The main ingredient is lamb, supplemented by carrot stewed into. Lamb of warm, suitable for winter consumption.",
        title="Braised mutton in brown sauce",
        url="http://127.0.0.1:8000/media/food_images/8.jpg")

    add_food(
        foodid=9,
        style=hot_style,
        cat = chicken_cat,
        likes = 8,
        description="Kung Pao Chicken is a spicy stir-fry dish made with chicken, peanuts, vegetables, and chili peppers. The classic dish in Sichuan cuisine originated in the Sichuan Province of south-western China and includes Sichuan peppercorns. Although the dish is found throughout China, there are regional variations that are typically less spicy than the Sichuan serving. Kung Pao chicken is also a staple of westernized Chinese cuisine.",
        title="Kung pao chicken",
        url="http://127.0.0.1:8000/media/food_images/9.jpg")

    add_food(
        foodid=10,
        style=sour_style,
        cat = other_cat,
        likes = 55,
        description="A deluxe pot of braised shiitake mushrooms, dried scallops, dried oysters and abalone. For this dish, I think it's important to marinate the mushrooms first and cook them separately instead of dumping everything into the pot and simply start braising.",
        title="Braised Mushrooms in Abalone Sauce",
        url="http://127.0.0.1:8000/media/food_images/10.jpg")

    add_food(
        foodid=11,
        style=salty_style,
        cat = chicken_cat,
        likes = 25,
        description="Steaming is such an ideal method to cook chicken. It allows us to cook our chicken without using too much oil. Chinese steamed chicken is simple, quick and the meat is always so tender in texture.",
        title="Steamed Chicken with Stuffing",
        url="http://127.0.0.1:8000/media/food_images/11.jpg")

    add_food(
        foodid=12,
        style=salty_style,
        cat = other_cat,
        likes = 34,
        description="Wash lotus root and cut into pieces.Saute garlic in oil. Add lotus root,Chinese mushrooms and stir well. Add Lee Kum Kee Premium Oyster Sauce, Lee Kum Kee Premium Dark Soy Sauce,  Sesame Oil and leek.  Cook for about 15 minutes.",
        title="Stewed Assorted Mushrooms with Lotus Roots",
        url="http://127.0.0.1:8000/media/food_images/12.jpg")

    add_food(
        foodid=13,
        style=sweet_style,
        cat = vegetables_cat,
        likes = 45,
        description="This is a dish we used to order in restaurant. The sweet taste mixed with the salted egg yolk is just perfect. And it is fairly easy to make.",
        title="Golden Corn",
        url="http://127.0.0.1:8000/media/food_images/13.jpg")

    add_food(
        foodid=14,
        style=sour_style,
        cat = vegetables_cat,
        likes = 22,
        description="Celery and celery has the same nutrition and therapy value. Celery of cool, sweet. Containing aromatic oil, VP and a variety of vitamins, amino acids and other substances, can promote appetite, reduce blood pressure, brain, facilitate bowel, detoxification swelling, promote blood circulation and other functions. Experiments show that celery has obvious antihypertensive effect, its duration increased with intake. And there is a sedative and anticonvulsant efficacy.",
        title="Sauteed Lily Bulbs and Celery",
        url="http://127.0.0.1:8000/media/food_images/14.jpg")

    add_food(
        foodid=15,
        style=sour_style,
        cat = vegetables_cat,
        likes = 31,
        description="That is the best kind of cooking after all. After steaming, the steamed tofu and vegetables can be drizzled with any vinaigrette your heart desires. This dish may be served family style placed in the center or in individual portions as shown here. It is delicious with steamed rice. Do give a try.",
        title="Steamed Tofu with Vegetables",
        url="http://127.0.0.1:8000/media/food_images/15.jpg")

    add_food(
        foodid=16,
        style=hot_style,
        cat = vegetables_cat,
        likes = 42,
        description="Mapo tofu is a popular Chinese dish from Sichuan province. It consists of tofu set in a spicy chili- and bean-based sauce, typically a thin, oily, and bright red suspension, and often cooked with douchi (fermented black beans) and minced meat, usually pork or beef. Variations exist with other ingredients such as water chestnuts, onions, other vegetables, or wood ear fungus.",
        title="Mapo Tofu",
        url="http://127.0.0.1:8000/media/food_images/16.jpg")

    add_food(
        foodid=17,
        style=sweet_style,
        cat = other_cat,
        likes = 26,
        description="Rice pudding is the Han nationality traditional name, Laba Festival custom. Popular in the country, especially in south of the Yangtze river. The same throughout the formulation, is basically a steamed glutinous rice mixed with sugar, oil, appliances and sweet scented osmanthus, poured with red dates, barley, lotus seeds, longan, fruit inside, steamed and then pour the sugar into the marinade. Taste sweet, is a holiday and guests to share.",
        title="Eight Delicacies Rice",
        url="http://127.0.0.1:8000/media/food_images/17.jpg")

    add_food(
        foodid=18,
        style=sour_style,
        cat = other_cat,
        likes = 39,
        description="This recipe comes from long practice and much experimentation.A year in China taught me the basics,and then I started modifying it at home until I was really satisfied with the results. Jiaozi are a kind of Chinese dumpling, commonly eaten across Eastern, Central, Southern and Western Asia. Though considered part of Chinese cuisine, jiaozi are popular and often eaten in many other Asian and Western countries. Jiaozi typically consist of a ground meat and/or vegetable filling wrapped into a thinly rolled piece of dough, which is then sealed by pressing the edges together or by crimping.",
        title="JiaoZi",
        url="http://127.0.0.1:8000/media/food_images/18.jpg")

    add_food(
        foodid=20,
        style=salty_style,
        cat = starters_cat,
        likes = 14,
        description="Try this delicious combination of seaweed and shiitake mushrooms to add six extra materials, especially iodine, to your Healthiest Way of Eating. Enjoy!",
        title="Seaweed Soup of Eight Delicacies",
        url="http://127.0.0.1:8000/media/food_images/19.jpg")

    add_food(
        foodid=19,
        style=hot_style,
        cat = fish_cat,
        likes = 16,
        description="They are delicious when braised or in steamboat, but one of my favourite ways of eating it is to make fish maw soup, like those chunky shark fin soup served during Chinese wedding dinners. Another good news for fish maw lovers is that it is said to be high in collagen.",
        title="Abalone and Shark's Fin with Fish Maw Soup",
        url="http://127.0.0.1:8000/media/food_images/20.jpg")

    add_food(
        foodid=21,
        style=sweet_style,
        cat = starters_cat,
        likes = 19,
        description="This sweet ferment rice (fermented glutinous rice) is Chinese yeast fermented glutinous rice or glutinous rice wine. It is low in alcohol content and tastes sweet, with a subtle wine aroma. Basically, make and boil tiny glutinous rice balls or dumplings. Then add the sweet ferment rice into the gently simmering water. Add gojiberries for some sweet overtone, or Osmanthus for aroma.",
        title="Glutinous Rice Dumplings in Fermented Rice Wine",
        url="http://127.0.0.1:8000/media/food_images/21.jpg")

    add_food(
        foodid=22,
        style=sour_style,
        cat = starters_cat,
        likes = 48,
        description="For breakfast, with a cup of tea, or packed in a lunchbox, these fluffy, fruity muffins from Andy McLeish have delicious nuggets of white chocolate hidden inside and a crunchy oat topping. Any seasonal berries would work well in these muffins, but frozen berries are a good option when they're not in season.",
        title="Mixed Fruit Muffin",
        url="http://127.0.0.1:8000/media/food_images/22.jpg")

    add_food(
        foodid=23,
        style=sour_style,
        cat = sidedishes_cat,
        likes = 25,
        description="This seaweed salad is a healthy  dish. It's sustainable and loaded with nutrients like fiber, vitamins and minerals like iron. Food blogger Marc Matsumoto explains where to purchase seaweed in a full post on the Fresh Tastes blog.",
        title="Seaweed Salad",
        url="http://127.0.0.1:8000/media/food_images/23.jpg")

    add_food(
        foodid=24,
        style=sour_style,
        cat = sidedishes_cat,
        likes = 37,
        description="The basic information English Name: Chinese Broccoli with Wasabi material: kale a small, ice packs a (homemade), mustard not + soy sauce dishes.",
        title="Chinese Broccoli with Wasabi",
        url="http://127.0.0.1:8000/media/food_images/24.jpg")

    add_food(
        foodid=25,
        style=hot_style,
        cat = duck_cat,
        likes = 40,
        description="Peking Duck is a famous duck dish from Beijing that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook. Ducks bred specially for the dish are slaughtered after 65 days and seasoned before being roasted in a closed or hung oven. The meat is eaten with scallion, cucumber and sweet bean sauce with pancakes rolled around the fillings. Sometimes pickled radish is also inside, and other sauces (like hoisin sauce) can be used.",
        title="Peking Roast Duck",
        url="http://127.0.0.1:8000/media/food_images/25.jpg")






    # Print out what we have added to the user.
def add_food(style,cat,title, url,likes,description,foodid):
    p = Food.objects.get_or_create(style=style,category=cat,title=title,foodid=foodid)[0]
    p.url=url
    p.likes=likes
    p.description=description
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

def add_style(name):
    d = Style.objects.get_or_create(name=name)[0]
    return d

# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()