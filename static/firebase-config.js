import {initializeApp} from "https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js";
import {getAuth,
    GoogleAuthProvider} from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
import {getFirestore} from "https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js";

// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyDyAUIAAPt5SXb455Ce_GupG1l1zk2vnCM",
    authDomain: "crudif-27b66.firebaseapp.com",
    projectId: "crudif-27b66",
    storageBucket: "crudif-27b66.firebasestorage.app",
    messagingSenderId: "153647829867",
    appId: "1:153647829867:web:8e4c09cfcd5589465d722e",
    measurementId: "G-BSE92SR7CW"
  };

  // Initialize Firebase
  const app = initializeApp(firebaseConfig);
  const auth = getAuth(app);
  const provider = new GoogleAuthProvider();
  
  const db = getFirestore(app);
  
  export { auth, provider, db };