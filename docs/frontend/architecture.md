# Frontend Architecture

## Technology Stack
- React 18+
- CSS3 with modern features
- Vite build system
- REST API integration

## Component Structure
```
components/
├── common/          # Shared components
│   ├── Button/
│   ├── Input/
│   └── Card/
│
├── layout/          # Layout components
│   ├── Header/
│   ├── Sidebar/
│   └── Footer/
│
└── features/        # Feature-specific components
    ├── appointments/
    ├── messaging/
    └── profile/
```

## Styling Approach
- Modern CSS using CSS Modules
- Responsive design principles
- Mobile-first approach
- Consistent color scheme and typography

## State Management
- React Context for global state
- Local component state
- Custom hooks for shared logic

## API Integration
- Axios for API requests
- Custom hooks for data fetching
- Error handling middleware
- Authentication interceptors
