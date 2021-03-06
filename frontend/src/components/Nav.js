import React from 'react'; // ES6 js
import {Link} from 'react-router-dom';

function Nav() {
    return(
        <nav class="navbar navbar-expand-lg navbar-dark">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navMainMenu" aria-controls="navMainMenu" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div id="navMainMenu" class="navbar-collapse collapse">
                <div class="navbar-nav">
                    <Link to='/' className="nav-item nav-link">Home</Link>
                    <Link to='/scenario1' className="nav-item nav-link">Income</Link>
                    <Link to='/scenario2' className="nav-item nav-link">Unemployment</Link>
                    <Link to='/scenario3' className="nav-item nav-link">Support</Link>
                    <Link to='/scenario4' className="nav-item nav-link">Live Stream Sentiment</Link>
                </div>
            </div>
        </nav>
    );
}

export default Nav;
