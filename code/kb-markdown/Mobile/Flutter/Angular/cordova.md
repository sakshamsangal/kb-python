# install package

```bash
npm install cordova -g
cordova -v
cordova create LeavePlan com.saksham.app "LeavePlan"
cordova platform add browser
cordova run browser

```

# connect with angular

# In angular project add to index.html

<script type='text/javascript' src='cordova.js'></script>

ng build --prod --base-href . --output-path ../../cordova/leave/www/

```javascript
In main.ts
let onDeviceReady = () => {
  platformBrowserDynamic().bootstrapModule(AppModule);
};
document.addEventListener('deviceready', onDeviceReady, false);

````

# run on mobile

```bash
ng build --prod --base-href . --output-path ../../cordova/LeavePlan/www/
cordova platform add android
cordova run android