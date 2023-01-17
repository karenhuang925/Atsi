import React from "react";
import { useSelector } from "react-redux";
import './PlaceOrder.css'

const PlaceOrder = () => {
    const user = useSelector(state => state.session.user);
    if (!user) return null

    return (
            <div className="contain">
                <div className="congrats py-8 flex-row ">
                    <h1 className="py-3">Congrat<span className="hide">ulation</span>s !</h1>
                    <div className="text">
                        <p>{user.first_name}, you have placed the order
                        </p>
                    </div>
                    <p className="text">Thank you</p>
                    <p className="regards mt-10">Atsi Team</p>
                </div>
            </div>

    )
}

export default PlaceOrder
