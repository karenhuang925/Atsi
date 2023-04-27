## Technologies
- Flask
- React
- Redux
- Tailwind CSS

## Quick Links
- [Database Schema](https://github.com/karenhuang925/Atsi/wiki/Schema)
- [API Documentation](https://github.com/karenhuang925/Atsi/wiki/API-docs)
- [Feature List](https://github.com/karenhuang925/Atsi/wiki/Feature-List)
- [Live Site](https://atsi.onrender.com/)

## Homepage screenshot
![Screen Shot 2023-01-17 at 00 51 56](https://user-images.githubusercontent.com/92420431/212852252-ae26b8ab-e61a-4bc7-a7cb-29e7a4d3addf.png)

## Product detail page screenshot
![Screen Shot 2023-01-17 at 00 52 53](https://user-images.githubusercontent.com/92420431/212852457-3a4620c8-8d48-4abe-ad19-c2c763baa214.png)

## Cart screenshot
![Screen Shot 2023-01-17 at 00 54 33](https://user-images.githubusercontent.com/92420431/212852789-c0259052-a9aa-4ecf-936d-6f4d60cf8b10.png)

## Setup

1. Clone the repository
2. In the root folder, create a .env file as below:

```
SECRET_KEY=«generate_strong_secret_here»
DATABASE_URL=sqlite:///dev.db
```

2. Run "pipenv install --dev -r dev-requirements.txt && pipenv install -r requirements.txt" in the app folder
3. Run "pipenv shell" in the app folder
4. Run "flask db upgrade" in the app folder
5. Run "flask db seed all" in the app folder
6. Run "flask run" in the app folder
7. Run "npm install" in the react-app folder
8. Run "npm start" in the react-app folder

## Future Features

- [ ] Search
- [ ] Product under certain category 
- [ ] AWS upload image
- [ ] Shop page
- [ ] Socket messaging 
