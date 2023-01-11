import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { PaperClipIcon } from '@heroicons/react/20/solid'


const Profile = () => {
    const user = useSelector(state => state.session.user);
    if (!user) return null

    return (
    <div className="overflow-hidden bg-white shadow sm:rounded-lg px-10 py-10">
        <div className="px-4 py-5 sm:px-6">
        <h3 className="text-xl font-medium leading-6 text-gray-900">Hi {user.first_name} {user.last_name}!</h3>
        <p className="mt-1 max-w-2xl text-base text-gray-500">View Public Profile Here</p>
        </div>
        <div className="border-t border-gray-200">
        <dl>
            <div className="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
            <dt className="text-base font-medium text-gray-500">Profile picture</dt>
            <dd className="mt-1 text-base text-gray-900 sm:col-span-2 sm:mt-0">
                <img src={user.preview_image} className='inline-block h-12 w-12 rounded-full ring-2 ring-white'/>
            </dd>
            </div>
            <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
            <dt className="text-base font-medium text-gray-500">Full name</dt>
            <dd className="mt-1 text-base text-gray-900 sm:col-span-2 sm:mt-0">{user.first_name} {user.last_name}</dd>
            </div>
            <div className="bg-white px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
            <dt className="text-base font-medium text-gray-500">Shop Name</dt>
            <dd className="mt-1 text-base text-gray-900 sm:col-span-2 sm:mt-0">{user.shop_name}</dd>
            </div>
            <div className="bg-gray-50 px-4 py-5 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-6">
            <dt className="text-base font-medium text-gray-500">Location</dt>
            <dd className="mt-1 text-base text-gray-900 sm:col-span-2 sm:mt-0">{user.location}</dd>
            </div>
        </dl>
        </div>
    </div>
    )
}

export default Profile
