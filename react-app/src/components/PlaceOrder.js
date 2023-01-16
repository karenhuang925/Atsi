import React from "react";
import { useSelector } from "react-redux";
import './PlaceOrder.css'

const PlaceOrder = () => {
    const user = useSelector(state => state.session.user);
    if (!user) return null

    return (
            <div className="contain">
                <div className="congrats">
                    <h1>Congrat<span className="hide">ulation</span>s !</h1>
                        <div className="text">
                            <p>{user.first_name}, you have placed the order
                            </p>
                        </div>
                    <p className="regards">Atsi Team</p>
                </div>
            </div>

    )
}

export default PlaceOrder
