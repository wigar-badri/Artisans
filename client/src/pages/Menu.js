import React, {useState} from 'react'
import MenuCategory from '../components/MenuCategory'
import items from '../components/MenuItems'

const allCategories = ["all", ...new Set(items.map((item) => item.category))]

function Menu () {
    const [menuItems, setMenuItems] = useState(items);
    const [activeCategory, setActiveCategory] = useState("");
    const [categories, setCategories] = useState(allCategories);
  
    const filterItems = (category) => {
      setActiveCategory(category)
      if (category === "all") {
        setMenuItems(items)
        return
      }
      const newItems = items.filter((item) => item.category === category)
      setMenuItems(newItems)
    }

    return (
        <main>
            <section className="menu section">
            <div className="title">
                <h2>Menus</h2>
                <div className="underline"></div>
            </div>
            <MenuCategory
                categories={categories}
                activeCategory={activeCategory}
                filterItems={filterItems}
            />
            <Menu items={menuItems} />
            </section>
      </main>
    )
}

export default Menu