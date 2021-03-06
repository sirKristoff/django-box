# Box service

Item organizing system for home storages.


## Basic functionality

- Collect _item categories_ descriptions including pictures.
- Collect _packages_ for storing physical _items_.
- Show relations between _packages_ and contained _items_ in them.


### _Items_ functionality

- [x] Named _Item category_ describe physical item instance and consists its picture.
- [x] _Item_ is searchable by content of its attributes (name, description).
- [ ] _Item category_ consists lists of _Packages_ containing physical item with category.
- [ ] _Item_ may be (un)assigned to _Package_ instance.
- [ ] _Item_ may be moved from one _Package_ instance to another.
- [ ] _Item_ has its QR code linking to _details_ page.
- [ ] _Item_ has breadcrumb info about _Package_ is stored in and "_parent_" _Packages_ containing primary _Package_.


### _Packages_ functionality

- [ ] _Packages_ are numbered and have its pictures.
- [ ] _Package_ consists list of included physical items.
- [ ] One _Package_ may be included in another.
- [ ] If _Package_ is included in another then it acts as item.
- [ ] Included _Items_ may be added or removed from _Package_.
- [ ] Included _Item_ may be moved from one _Package_ to another.
- [ ] _Package_ has its QR code linking to _details_ page.
- [ ] _Package_ has breadcrumb info about _Package_ is stored in and "_parent_" _Packages_ containing primary _Package_.


## TODO

**`card.html`**
- [ ] Make inline item details as horizontal card with small image
- [ ] For full item details use fancy buttons for _Edit_ and _Delete_

**`searchbar.html`**
- [ ] Change single `input` to `input-group`

**`item/update.html`**
- [ ] Refactor buttons (`Save`, `Save and continue`, `Back`) on _Update_ page

**`test-data/`**
- [ ] Clear history (`django_admin_log`) of operations on example data
