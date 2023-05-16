```
First check node and npm is installed or not using following commands
node -v
npm -v

--skip-tests' instead of '--skipTests'.

Now do: npm install -g @angular/cli
then: ng new my-app
then: cd my-app
then: ng serve --open

node -v
ng --version
npm install @angular/cli@latest
ng new hello
cd hello
npm install bootstrap --save
"node_modules/bootstrap/dist/css/bootstrap.min.css"
ng build
ng serve -open -port 4200
ng serve

ng g s services/general

ng g cl models/person
ng g c components/spinner

ng g c components/home
ng g c components/page1
ng g c components/page2
ng g c components/page3
ng g c components/page4
ng g c components/page5
ng g c components/display-delete

ng g c components/display
ng g c components/update
ng g c components/delete
ng g c components/insert
ng g c components/page-not-found

npm install -g @angular/cli
npm install -g @angular/cli@latest // optional

ng new app-demo
ng serve

for %n in (home, page1, page2, page3) do ng g c components/%n -is --skipTests

for i in page1 page2 page3 page4; do ng g c comp/"${i}" -is --skip-tests; done
for i in shopping-list; do ng g s service/"${i}" --skip-tests; done

for i in shopping-list shopping-edit; do ng g c components/"${i}" -is --skip-tests; done

for i in dropdown; do ng g d directive/"${i}" --skip-tests; done

```