import React from "react";
import { NavLink } from "react-router-dom";
import './Footer.css'
  
const Footer = () => {
  return (
    <div className="box flex-col">
        <h1 className="text-2xl text-center text-blue-700 mb-10">About Me</h1>
        <div className="flex">
            <div className="text-lg w-48 mr-10">Karen is a full-stack software engineer based in the San Francisco Bay Area</div>
            <div className="flex-col w-20">
                <div className="text-lg">Social Media</div>
                <a href='https://github.com/karenhuang925' >
                    <i class="fa-brands fa-github"></i>Github
                </a>
                <a href='https://www.linkedin.com/in/karen-huang-274b5b10b/'>
                    <i class="fa-brands fa-linkedin"></i>Linkedin
                </a>
            </div>
        </div>
    </div>
  );
};
export default Footer;